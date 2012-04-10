from bottle import route, run, template, redirect, request
from datetime import timedelta, datetime
import os
import oursql
#import jsonp_bottle

# TODO: timestamp


def parse_date_string(stamp):
    return datetime.strptime(stamp, '%Y%m%d%H%M%S')


class ArticleHistory:
    '''article history object'''
    def __init__(self, title, namespace=0):
        db = oursql.connect(db='enwiki_p',
            host="enwiki-p.rrdb.toolserver.org",
            read_default_file=os.path.expanduser("~/.my.cnf"),
            charset=None,
            use_unicode=False)
        cursor = db.cursor(oursql.DictCursor)
        cursor.execute('''
            SELECT      revision.rev_user_text, revision.rev_timestamp, revision.rev_user, revision.rev_minor_edit, revision.rev_len, revision.rev_deleted, revision.rev_comment, page.page_id, page.page_title
            FROM        revision
            INNER JOIN  page ON revision.rev_page = page.page_id
            WHERE       page_title = ? AND page.page_namespace = ?;
            ''', (title, namespace))
        self.revisions = cursor.fetchall()
        self.first_edit_date = parse_date_string(self.revisions[0]['rev_timestamp'])
        self.age = datetime.now() - self.first_edit_date
        self.most_recent_edit_date = parse_date_string(self.revisions[-1]['rev_timestamp'])
        self.most_recent_edit_age = datetime.now() - self.most_recent_edit_date

    def get_by_period(self, year, month=0):
        by_period = []
        if month == 0:
            for rev in self.revisions:
                if rev['rev_timestamp'][:4] == str(year):
                    by_period.append(rev)
        else:
            for rev in self.revisions:
                if rev['rev_timestamp'][:6] == str(year) + str(month).zfill(2):
                    by_period.append(rev)
        return by_period

    def get_since(self, day_limit):
        recent_revs = []
        threshold = datetime.now() - timedelta(days=day_limit)
        for rev in self.revisions:
            if parse_date_string(rev['rev_timestamp']) > threshold:
                recent_revs.append(rev)
        return recent_revs

    def get_average_time_between_edits(self, revisions=None):
        times = []
        if revisions == None:
            revisions = self.revisions
        for rev in revisions:
            times.append(parse_date_string(rev['rev_timestamp']))
        time_diffs = []
        for i, time in enumerate(times):
            if time == times[0]:
                continue
            else:
                time_diffs.append(time - times[i - 1])
        if len(time_diffs) != 0:
            return str(sum(time_diffs, timedelta(0)) / len(time_diffs))
        else:
            return None

    def get_average_length(self, revisions=None):
        if revisions == None:
            revisions = self.revisions
        if len(revisions) != 0:
            return sum([rev['rev_len'] for rev in revisions]) / len(revisions)
        return None

    def get_revert_estimate(self, revisions=None):
        reverts = 0
        if revisions == None:
            revisions = self.revisions
        for rev in revisions:
            if 'revert' in rev['rev_comment'].lower():
                reverts += 1
        return reverts

    def get_revision_total(self, revisions=None):
        if revisions == None:
            revisions = self.revisions
        return len(revisions)

    def get_minor_count(self, revisions=None):
        if revisions == None:
            revisions = self.revisions
        return sum([rev['rev_minor_edit'] for rev in revisions])

    def get_anon_count(self, revisions=None):
        anon_count = 0
        if revisions == None:
            revisions = self.revisions
        for rev in revisions:
            if rev['rev_user'] == 0:
                    anon_count += 1
        return anon_count

    def get_editor_counts(self, revisions=None):
        authors = {}
        if revisions == None:
            revisions = self.revisions
        for rev in revisions:
            user = rev['rev_user_text']
            if user in authors:
                authors[user] += 1
            else:
                authors[user] = 1
        return authors

    def get_some_editors(self, num, revisions=None):
        if revisions == None:
            revisions = self.revisions
        authors = self.get_editor_counts(revisions)
        return dict([(a, c) for (a, c) in authors.items() if c > num])

    def get_top_editors(self, revisions=None):
        if revisions == None:
            revisions = self.revisions
        authors = self.get_editor_counts(revisions)
        return sorted(authors.iteritems(), key=lambda (k, v): v, reverse=True)

    def get_top_percent_editors(self, top=.20, revisions=None):
        if revisions == None:
            revisions = self.revisions
        editors = self.get_editor_counts(revisions)
        if(len(editors)) != 0:
            threshold = int(round(len(editors) * top))
            top_editors = self.get_top_editors(revisions)[:threshold]
            total = sum([v for (k, v) in top_editors], 0)
            return total / float(self.get_revision_total(revisions))
        else:
            return None

    def get_editor_count(self, revisions=None):
        if revisions == None:
            revisions = self.revisions
        return len(self.get_editor_counts(revisions))


@route('/revisions/<title>')
def get_revisions(title):
    article = ArticleHistory(title)
    stats = {'total_revisions':             article.get_revision_total(),
            'minor_count':                  article.get_minor_count(),
            'IP_edit_count':                article.get_anon_count(),
            'first_edit':                   str(article.first_edit_date),
            'most_recent_edit':             str(article.most_recent_edit_date),
            'average_time_between_edits':   article.get_average_time_between_edits(),
            'age':                          str(article.age),
            'recent_edit_age':              str(article.most_recent_edit_age),
            'editors_five_plus_edits':      len(article.get_some_editors(5)),
            'top_20_percent':               article.get_top_percent_editors(),
            'top_5_percent':                article.get_top_percent_editors(.05),
            'total_editors':                article.get_editor_count(),
            'average_length':               article.get_average_length(),
            'reverts_estimate':             article.get_revert_estimate(),
            'last_30_days_total_revisions': article.get_revision_total(article.get_since(30)),
            'last_30_days_minor_count':     article.get_minor_count(article.get_since(30)),
            'last_30_days_IP_edit_count':   article.get_anon_count(article.get_since(30)),
            'last_30_days_average_time_between_edits': article.get_average_time_between_edits(article.get_since(30)),
            'last_30_days_editors_five_plus_edits': len(article.get_some_editors(5, article.get_since(30))),
            'last_30_days_top_20_percent':  article.get_top_percent_editors(.20, article.get_since(30)),
            'last_30_days_top_5_percent':   article.get_top_percent_editors(.05, article.get_since(30)),
            'last_30_days_total_editors':   article.get_editor_count(article.get_since(30)),
            'last_30_days_average_length':  article.get_average_length(article.get_since(30)),
            'last_30_days_reverts_estimate': article.get_revert_estimate(article.get_since(30)),
            'last_500_total_revisions':     article.get_revision_total(article.revisions[:500]),
            'last_500_minor_count':         article.get_minor_count(article.revisions[:500]),
            'last_500_IP_edit_count':        article.get_anon_count(article.revisions[:500]),
            'last_500_average_time_between_edits': article.get_average_time_between_edits(article.revisions[:500]),
            'last_500_editors_five_plus_edits': len(article.get_some_editors(5, article.revisions[:500])),
            'last_500_top_20_percent':      article.get_top_percent_editors(.20, article.revisions[:500]),
            'last_500_top_5_percent':       article.get_top_percent_editors(.05, article.revisions[:500]),
            'last_500_total_editors':       article.get_editor_count(article.revisions[:500]),
            'last_500_average_length':      article.get_average_length(article.revisions[:500]),
            'last_500_reverts_estimate':    article.get_revert_estimate(article.revisions[:500])
            }
    return stats


@route('/history/search/')
def search():
    redirect('/history/en/wp/' + request.query.title)


@route('/history/<language>/<project>/<title>')
def get_history(title, language, project):
    title = title.replace('%20', '_')
    title = title.replace(' ', '_')
    article = ArticleHistory(title)
    stats = {'title':                       title,
            'total_revisions':             article.get_revision_total(),
            'minor_count':                  article.get_minor_count(),
            'IP_edit_count':                article.get_anon_count(),
            'first_edit':                   str(article.first_edit_date),
            'most_recent_edit':             str(article.most_recent_edit_date),
            'average_time_between_edits':   article.get_average_time_between_edits(),
            'age':                          str(article.age),
            'recent_edit_age':              str(article.most_recent_edit_age),
            'editors_five_plus_edits':      len(article.get_some_editors(5)),
            'total_editors':                article.get_editor_count(),
            'average_length':               article.get_average_length(),
            'reverts_estimate':             article.get_revert_estimate(),
            'last_day':                     article.get_revision_total(article.get_since(1)),
            'last_7_days':                  article.get_revision_total(article.get_since(7)),
            'last_30_days':                 article.get_revision_total(article.get_since(30)),
            'last_365_days':                article.get_revision_total(article.get_since(365)),
            'top_5_percent':                article.get_top_percent_editors(.05),
            'top_10_percent':                article.get_top_percent_editors(.10),
            'top_20_percent':                article.get_top_percent_editors(.20),
            'top_30_percent':                article.get_top_percent_editors(.30),
            'top_40_percent':                article.get_top_percent_editors(.40),
            'top_50_percent':                article.get_top_percent_editors(.50)
            }
    '''first_year = article.revisions[0]['rev_timestamp'][:4]
    first_month = article.revisions[0]['rev_timestamp'][4:6]
    last_year = article.revisions[-1]['rev_timestamp'][:4]
    last_month = article.revisions[-1]['rev_timestamp'][4:6]
    stats['by_month'] = []
    stats['by_year'] = []
    for y in range(int(first_year), int(last_year) + 1):
        if y == first_year:
            start = first_month
        else:
            start = 1
        if y == last_year:
            end = last_month
        else:
            end = 13
        for m in range(int(start), int(end)):
            revs = article.get_by_period(y, m)
            label = str(y) + '/' + str(m)
            stats['by_month'].append({'range': label,
                                 'values': {'total_revisions':              article.get_revision_total(revs),
                                            'minor_count':                  article.get_minor_count(revs),
                                            'IP_edit_count':                article.get_anon_count(revs),
                                            'average_time_between_edits':   article.get_average_time_between_edits(revs),
                                            'editors_five_plus_edits':      len(article.get_some_editors(5, revs)),
                                            'total_editors':                article.get_editor_count(revs),
                                            'average_length':               article.get_average_length(revs),
                                            'reverts_estimate':             article.get_revert_estimate(revs)}})
        y_revs = article.get_by_period(y)
        stats['by_year'].append({'range': str(y),
                                'values': {'total_revisions':              article.get_revision_total(y_revs),
                                            'minor_count':                  article.get_minor_count(y_revs),
                                            'IP_edit_count':                article.get_anon_count(y_revs),
                                            'average_time_between_edits':   article.get_average_time_between_edits(y_revs),
                                            'editors_five_plus_edits':      len(article.get_some_editors(5, y_revs)),
                                            'total_editors':                article.get_editor_count(y_revs),
                                            'average_length':               article.get_average_length(y_revs),
                                            'reverts_estimate':             article.get_revert_estimate(y_revs)}})'''
    stats['top_editors'] = article.get_top_editors()[:50]
    return template('en', stats)

if __name__ == '__main__':
    run(host='0.0.0.0', port=8088, reloader=True, debug=True)
