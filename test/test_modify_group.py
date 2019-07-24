from random import randrange

from model.group import Group


def test_modify_group_name(gg):
    if gg.group.count() == 0:
        gg.group.create(Group(name="test"))
    old_groups = gg.group.get_group_list()
    index = randrange(len(old_groups))
    group=Group(name="New group")
    group.id=old_groups[index].id
    gg.group.modify_group_by_index(index,group)
    new_groups = gg.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index]=group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_group_header(app):
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="New header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)

