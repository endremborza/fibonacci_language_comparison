import os
import json
import dash
from dash.dependencies import Input, Output, State
import dash_table
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Interval(
        id='interval-component',
        interval=5 * 1000,  # in milliseconds
        n_intervals=0
    ),
    html.Div([
        dcc.Input(
            id='add-contestant-name',
            placeholder='Add contestant',
            value='',
            style={'padding': 10}
        ),
        html.Button('Add Contestant', id='add-contestant-button', n_clicks=0)
    ], style={'height': 50}),

    dash_table.DataTable(
        id='contestants-table',
        columns=[{
            'name': cid,
            'id': cid.lower(),
            'deletable': False,
            'editable': False
        } for cid in ['Command', 'Outcome']],
        data=[],
        editable=True,
    ),

    html.Div([html.H2('Leaderboard'),
              html.Div(id='leaderboard')])
])


@app.callback(
    Output('contestants-table', 'columns'),
    [Input('add-contestant-button', 'n_clicks')],
    [State('add-contestant-name', 'value'),
     State('contestants-table', 'columns')])
def update_columns(n_clicks, value, existing_columns):
    if n_clicks > 0:
        existing_columns.append({
            'id': value, 'name': value,
            'editable': True,
            'deletable': True
        })
    return existing_columns


@app.callback(
    Output('leaderboard', 'children'),
    [Input('contestants-table', 'data'),
     Input('contestants-table', 'columns')])
def display_output(rows, columns):
    pass

    contestants = columns[2:]
    contestant_scores = {k['name']: 0 for k in contestants}
    for r in rows:
        for c in contestant_scores.keys():
            try:
                contestant_scores[c] += abs(r['outcome'] - float(r[c])) / (r['outcome'] + float(r[c])) * 2
            except KeyError:
                pass
            except TypeError:
                pass
            except ValueError:
                pass

    board = sorted(contestant_scores.items(),
                   key=lambda x: x[1])

    out = []
    for rank, cs in enumerate(board):
        out.append(html.H4('{0:}. - {1:} ({2:0.2f}%)'.format(rank+1,
                                                             cs[0],
                                                             cs[1] * 100)))

    return html.Div(children=out)


@app.callback(
    Output('contestants-table', 'data'),
    [Input('interval-component', 'n_intervals')],
    [State('contestants-table', 'data')])
def refresh_data(_, data):
    print(data)
    try:
        with open(os.environ.get('DUMP_LOC', '/out.json')) as fp:
            times = json.load(fp)
    except FileNotFoundError:
        times = [{}] * len(data)
    print(times)
    if len(data) < len(times):
        data = [{}] * len(times)

    new_data = []
    for t, r in zip(times, data):
        new_data.append({**r, **t})

    return new_data


if __name__ == '__main__':
    app.run_server(debug=True,
                   host='0.0.0.0',
                   port=os.environ.get("PORT_NO"))
