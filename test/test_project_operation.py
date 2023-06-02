import time

def test_add_project(app):
    project_name = app.testdata["project"]
    app.session.menu_link_by_name("Manage")
    app.session.menu_link_by_name("Manage Projects")
    if app.soap.is_project_exists(project_name):
        assert False, 'Проект с именем %s уже существует' % project_name
    old_proj_list = app.soap.get_project_list()
    app.session.add_project(project_name)
    time.sleep(4)
    if app.soap.is_project_exists(project_name):
        assert True, 'Проект успешно добавлен %s' % project_name
    else:
        assert False, 'Ошибка при добавлении проекта %s' % project_name
    new_proj_list = app.soap.get_project_list()
    old_proj_list.append(project_name)
    assert sorted(old_proj_list) == sorted(new_proj_list)

def test_delete_project(app):
    project_name = app.testdata["project"]
    app.session.menu_link_by_name("Manage")
    app.session.menu_link_by_name("Manage Projects")
    if app.soap.is_project_exists(project_name) == False:
        assert False, 'Проект с именем %s не существует' % project_name
    old_proj_list = app.soap.get_project_list()
    app.session.delete_project(project_name)
    time.sleep(4)
    if app.soap.is_project_exists(project_name):
        assert False, 'Проект %s успешно удален ' % project_name
    else:
        assert True, 'Ошибка при удалении проекта %s' % project_name
    new_proj_list = app.soap.get_project_list()
    new_proj_list.append(project_name)
    assert sorted(old_proj_list) == sorted(new_proj_list)


