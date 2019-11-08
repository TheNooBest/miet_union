from admin_tools.dashboard import modules, Dashboard


class CustomIndexDashBoard(Dashboard):
    columns = 4
    title = ('Консоль администратора')

    def __init__(self, **kwargs):
        Dashboard.__init__(self, **kwargs)
        self.children.append(
            modules.ModelList(
                title=('Новости портала'),
                models=('news.models.News',),
            )
        )
        self.children.append(
            modules.ModelList(
                title=('Работники Профкома'),
                models=('ourteam.models.Worker',),
            )
        )
