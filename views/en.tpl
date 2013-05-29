      <h1>{{title_norm}}</h1>
      <p>Article revision details</p>
      <div class="subnav">
        <ul class="nav nav-pills">
          <li>
            <a href="#overview">Overview</a>
          </li>
          <li><a href="#yearly">Recent</a></li>
          <li><a href="#editors">Top 50 editors</a></li>
        </ul>
        </div>
      <a name="overview"></a><h2>General information</h2>
      <table class="table table-bordered table-striped">
        <thead>
          <tr>
            <th>Stat</th>
            <th>Value</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Total number of revisions</td>
            <td>

              {{total_revisions}}

            </td>
          </tr>
          <tr>
            <td>Total number of minor revisions</td>
            <td>

              {{minor_count}}

            </td>
          </tr>
          <tr>
            <td>Estimated number of reverts</td>
            <td>

              {{reverts_estimate}}

            </td>
          </tr>
          <tr>
            <td>Total number of IP (anonymous) revisions</td>
            <td>

              {{IP_edit_count}}

            </td>
          </tr>
          <tr>
            <td>Number of unique editors</td>
            <td>

              {{total_editors}}

            </td>
          </tr>
          <tr>
            <td>Number of editors with 5+ edits in this article</td>
            <td>

              {{editors_five_plus_edits}}

            </td>
          </tr>
          <tr>
            <td>First revision date</td>
            <td>

              {{first_edit}} ({{age}} ago)

            </td>
          </tr>
          <tr>
            <td>Most recent revision date</td>
            <td>

              {{most_recent_edit}} ({{recent_edit_age}} ago)

            </td>
          </tr>
          <tr>
            <td>Average time between revisions</td>
            <td>

              {{round(float(edit_interval_avg), 1)}} seconds <span id='edit_interval' style='float:right;'></span>

            </td>
          </tr>
          <tr>
            <td>Average size of the article</td>
            <td>

              {{avg_length}} bytes <span id='average_length' style='float:right;'></span>

            </td>
          </tr>
        </tbody>
      </table>
      <a name="revs"></a><h2>Recent edits</h2>
      <table class="table table-bordered table-striped">
        <thead>
          <tr>
            <th>Number of edits in</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>The last day</td>
            <td>

              {{last_day}}

            </td>
          </tr>
          <tr>
            <td>The last 7 days</td>
            <td>

              {{last_7_days}}

            </td>
          </tr>
          <tr>
            <td>The last 30 days</td>
            <td>

              {{last_30_days}}

            </td>
          </tr>
          <tr>
            <td>The last 365 days</td>
            <td>

              {{last_365_days}}

            </td>
          </tr>
        </tbody>
      </table>
      <a name="revs"></a><h2>Revision history</h2>
      <div id='chart'>
        <div id='monthly'></div>
        <script type="text/javascript">
        var monthly_revs = {{!monthly}};
        line_chart(monthly_revs, '#monthly');

        var edit_interval = {{!edit_interval_list}};
        spark_graph(edit_interval, '#edit_interval');

        var length_list = {{!length_list}};
        spark_graph(length_list, '#average_length');
        </script>
      </div>
      <a name="editors"></a><h2>Editors</h2>
      <h3>Diversity</h3>
      <ul>
        <li><strong>{{round(top_5_percent, 2) * 100}}%</strong> of the edits were made by 5% of the editors</li>
        <li><strong>{{round(top_20_percent, 2) * 100}}%</strong> of the edits were made by 20% of the editors</li>
        <li>Out of {{total_editors}} unique contributors, <strong>{{round(editors_five_plus_edits / (total_editors + 0.0), 2) * 100}}%</strong> made five or more edits to this article</li>
      </ul>
      <h3>Top 50 Editors</h3>
      <table class="table table-bordered table-striped">
        <thead>
          <tr>
            <th>Username</th>
            <th>Edits to "{{title}}"</th>
          </tr>
        </thead>
        <tbody>
%for  (k, v) in top_editors:
          <tr>
            <td><a href='http://en.wikipedia.org/wiki/User:{{k}}'>{{k}}</a></td>
            <td>

              {{v}}

            </td>
          </tr>
%end
        </tbody>
      </table>
       <body>
%rebase layout
