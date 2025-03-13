import plotly.express as px
import plotly.graph_objects as go


def create_pie_chart(df, column_name, title, mapping):
    grouped_df = df.groupby(by=[column_name], as_index=False)['Group'].count()

    custom_label = grouped_df[column_name].map(mapping)

    grouped_df['custom label'] = custom_label

    total_value = grouped_df['Group'].sum()

    fig = go.Figure(data = [go.Pie(
        labels=grouped_df['custom label'],
        values=grouped_df['Group'],
        textposition='inside',
        hole=.33,
        textinfo='percent',
        hoverinfo='label+value',
        direction='clockwise',
        marker=dict(
            colors=px.colors.sequential.Plasma
        )
    )])
    fig.update_layout(
        title = title,
        showlegend=False,
        annotations = [
            dict(
                x=1.0,
                y=1.05,
                xref = 'paper',
                yref = 'paper',
                text=f'Total: {total_value}',
                showarrow=False,
                font=dict(size=19),
                align='left',
            )
        ]
    )
    return fig


def create_bar_chart(df, column_name, mapping, title):
    grouped_df = df.groupby(by=[column_name], as_index=False)['Group'].count()

    custom_label = grouped_df[column_name].map(mapping)

    grouped_df['custom label'] = custom_label

    grouped_df = grouped_df.groupby('custom label', as_index=False)['Group'].sum()
    
    grouped_df = grouped_df.sort_values('Group', ascending=False)  # Sort the data in descending order by Group column

    total_value = grouped_df['Group'].sum()

    fig = px.bar(grouped_df, x='custom label', y='Group', template='seaborn', width=500, height=400)

    fig.update_xaxes(
        showticklabels=True, 
        tickangle=-45,
        title_text='', 

    )
 
    
    fig.update_yaxes(
        showticklabels=False,
        title_text='',   # Ẩn tiêu đề trục y
        showgrid=False
    )

    fig.update_traces(hovertemplate='%{x}<br>%{y}', width=0.5)  # Set a fixed width for the bars

    fig.update_layout(
        title = title,
        margin = dict(b = 150)
    )  # Ensure uniform text size

    for i in range(len(grouped_df)):
        fig.add_annotation(
            x=grouped_df['custom label'][i],
            y=grouped_df['Group'][i],
            text=str(grouped_df['Group'][i]),
            showarrow=False,
            yshift=10,
            font=dict(
                size=12,
            ),
            align = 'center'
        )

    fig.add_annotation(
        x = 0.5,
        y = 1.1,
        xref = 'paper',
        yref = 'paper',
        text = f'Total: {total_value}',
        showarrow = False,
        font = dict(size=15),
        align = 'center'
    )

    return fig


def pie_chart_by_max_line(df, mapping):    
    custom_label = df.iloc[: , 0].map(mapping)

    df['custom label'] = custom_label

    temp = df.copy()

    df = df.groupby(by=['custom label'], as_index=False)['Line'].count()

    df = df.sort_values('Line', ascending=False)

    max_val = df.iloc[0,0]

    temp = temp[temp['custom label'] == max_val]

    temp = temp['Line'].value_counts().reset_index()

    temp.columns = ['Line', 'Count']

    fig = px.pie(
        temp,
        values = 'Count',
        names = 'Line',
    )
    fig.update_traces(
        textinfo = 'percent+label',
        textposition = 'inside',
        textfont_size = 14
    )

    return fig
