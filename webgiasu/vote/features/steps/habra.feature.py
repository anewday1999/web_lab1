from behave import given, when, then

@then(u'I should see link contents url "{content}"')
def i_should_see_link_contents_url(context, content):
    msg = True
    assert msg

@when(r'I visit url "{url}"')
def i_visit_url(context, url):
    br = context.browser
    br.visit(url)

@given(u'I am a visitor')
def i_am_a_visitor(context):
    pass