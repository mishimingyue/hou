from jsonpath import jsonpath
from requests_1.tag import Tag
import datetime


class TestTag:
    def setup_class(self):
        self.tag = Tag()

    def test_list(self):
        m = self.tag.list()
        assert m.status_code == 200
        assert m.json()['errcode'] == 0

    def test_updata(self):
        tag_name = 'tag1_new_' + str(datetime.datetime.now().strftime("%Y%m%d-%H%M"))
        n = self.tag.update('etn1u6CQAAU8FmUE-eevWGL0VwiV260g', tag_name)
        assert n.status_code == 200
        assert n.json()['errcode'] == 0

    def test_list_update_list(self):
        # self.tag.list()
        tag_name = 'tag1_new_' + str(datetime.datetime.now().strftime("%Y%m%d-%H%M"))
        p = self.tag.update('etn1u6CQAAU8FmUE-eevWGL0VwiV260g', tag_name)
        q = self.tag.list()
        tags = [
            tag
            for group in q.json()['tag_group'] if group['group_name'] == 'python15'
            for tag in group['tag'] if tag['name'] == tag_name
        ]
        # jsonpath(f"$..[?(@.name='{tag_name}')]") jmepath
        assert tags != []

    def test_add_tag(self):
        group_name = "TMP00123"
        tag = [
            {"name": "TAG3"},
            {"name": "TAG2"},
            {"name": "TAG3"},
        ]

        r = self.tag.add(group_name=group_name, tag=tag)
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

    def test_add_and_detect(self):
        group_name = "TMP00123"
        tag = [
            {"name": "TAG1"},
            {"name": "TAG2"},
            {"name": "TAG3"},
        ]
        r = self.tag.add_and_detect(group_name, tag)
        assert r

    def test_delete_group(self):
        self.tag.delete_group(["etn1u6CQAAYOdz0XzsRCXx346lcu0L2Q"])

    def test_delete_tag(self):
        self.tag.delete_tag(["etn1u6CQAAU8FmUE-eevWGL0VwiV260g"])

    def test_delete_and_detect_group(self):
        r = self.tag.delete_and_detect_group(["etn1u6CQAAMi2W8wHuUaDeHoAytLdQVw"])
        assert r.json()["errcode"] == 0
