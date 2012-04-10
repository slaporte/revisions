      <h1>{{title}}</h1>
      <p>Article revision information</p>
      <h2>General numbers</h2>
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
            <td>Total number of IP revisions</td>
            <td>
            
              {{IP_edit_count}}
            
            </td>
          </tr>
          <tr>
            <td>First revision date</td>
            <td>
            
              {{first_edit}}
            
            </td>
          </tr>
          <tr>
            <td>Most recent revision date</td>
            <td>
            
              {{most_recent_edit}}
            
            </td>
          </tr>
          <tr>
            <td>Average time between revisions</td>
            <td>
            
              {{average_time_between_edits}}
            
            </td>
          </tr>
          <tr>
            <td>Article age</td>
            <td>
            
              {{age}}
            
            </td>
          </tr>
          <tr>
            <td>Age of the most recent revision</td>
            <td>
            
              {{recent_edit_age}}
            
            </td>
          </tr>
          <tr>
            <td>Number of editors with 5+ edits in this article</td>
            <td>
            
              {{editors_five_plus_edits}}
            
            </td>
          </tr>
          <tr>
            <td>Number of unique editors</td>
            <td>
            
              {{total_editors}}
            
            </td>
          </tr>
          <tr>
            <td>Average length of the article</td>
            <td>
            
              {{average_length}}
            
            </td>
          </tr>
          <tr>
            <td>Number of revisions in the last day</td>
            <td>
            
              {{last_day}}
            
            </td>
          </tr>
          <tr>
            <td>Number of revisions in the last 7 days</td>
            <td>
            
              {{last_7_days}}
            
            </td>
          </tr>
          <tr>
            <td>Number of revisions in the last 30 days</td>
            <td>
            
              {{last_30_days}}
            
            </td>
          </tr>
          <tr>
            <td>Number of revisions in the last 365 days</td>
            <td>
            
              {{last_365_days}}
            
            </td>
          </tr>
          <tr>
            <td>Percent of revisions from the top 5% of editors in this article</td>
            <td>
            
              {{top_5_percent}}
            
            </td>
          </tr>
          <tr>
            <td>Percent of revisions from the top 20% of editors in this article</td>
            <td>
            
              {{top_20_percent}}
            
            </td>
          </tr>
        </tbody>
      </table>
      <h2>Top editors</h2>
      <table class="table table-bordered table-striped">
        <thead>
          <tr>
            <th>Editor</th>
            <th>Edits to {{title}}</th>
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
%rebase layout