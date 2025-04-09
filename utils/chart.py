import plotly.graph_objects as go

def show_overdue_loans_graph(result, title):
    period = result['period']
    overdue_loans = result['overdue_loans']
    overdue_loans_share = result['overdue_loans_share']

    fig = go.Figure()

    # Overdue loans
    fig.add_trace(
        go.Scatter(
            x=period
            , y=overdue_loans
            , name='Overdue Loans'
            , yaxis='y1'
        )
    )

    # Overdue loans share
    fig.add_trace(
        go.Scatter(
            x=period
            , y=overdue_loans_share
            , name='Share (%)'
            , yaxis='y2'
            , line=dict(dash='dot', color='orange')
        )
    )

    # Add description to the graph
    fig.update_layout(
        title=title
        , xaxis=dict(title='Date')
        , yaxis=dict(title='Overdue Loans', side='left')
        , yaxis2=dict(
            title='Share (%)'
            , overlaying='y'
            , side='right'
            , showgrid=False
        )
        , legend=dict(x=0.01, y=0.99)
    )

    fig.show()
