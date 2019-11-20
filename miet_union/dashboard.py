from admin_tools.dashboard import modules, Dashboard


class CustomIndexDashBoard(Dashboard):
    columns = 3
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
        self.children.append(
            modules.ModelList(
                title=('Работники Профкома'),
                models=('miet_union.models.HelpForProforg',),
            )
        )
        self.children.append(
            modules.ModelList(
                title=('Пользователи'),
                models=('django.contrib.*',),
            ),
        )
        self.children.append(modules.Group(
            title=("Документы"),
            display="tabs",
            children=[
                modules.ModelList(
                    title=('Студенту'),
                    models=('documents.models.HelpForProforg',
                            'documents.models.HelpForStudentProforg',
                            'TheMainActivitiesOfProforg',),
                ),
                modules.ModelList(
                    title=('Документы'),
                    models=('documents.models.ProtectionOfPersonalInformation',
                            'documents.models.LegislativeRegulatoryAndStatutoryDocuments',
                            'documents.models.CommissionsOfProfcom',
                            'documents.models.UsefulLinks',),
                ),

            ]
        )
        )
