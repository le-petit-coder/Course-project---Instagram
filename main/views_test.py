from run import app
import pytest

key_data = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count",
            "pk"}


class Test_API:

    @pytest.fixture()
    def app_instance(self):
        return app.test_client()

    def test_post_page(self, app_instance):
        result = app_instance.get("/api/posts", follow_redirects=True)
        assert type(result.json) == list, "несоответствующий тип данных"
        assert result.status_code == 200, "Неправильный статус "

    def test_page_post_pk(self, app_instance):
        result = app_instance.get("/api/posts/1", follow_redirects=True)
        assert result.status_code == 200
        assert type(result.json) == dict, "несоответствующий тип данных"

