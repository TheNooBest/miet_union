from django.urls import reverse, resolve


class TestUrls:

    def test_news_page_url(self):
        path = reverse('news_page', kwargs={'pk': 1})
        assert resolve(path).view_name == 'news_page'
