from behave import given, when, then
from WeatherData import WeatherData

weather_obj = WeatherData()
@given(u'I like to holiday in "{city}" on "{day}"')
def step_impl(context, city, day):
    weather_obj.set_city(city)
    weather_obj.set_day(day)


@given(u'If today is "{day}"')
def step_impl(context, day):
    weather_obj.check_day(day)


@when(u'I look up the weather forecast')
def step_impl(context):
    context.current_weather_data = weather_obj.get_current_weather_data()
    context.temperature = context.current_weather_data["main"]["temp"]


@then(u'check the temperature is warmer than "{threshold}" degrees')
def step_impl(context, threshold):
    result = context.temperature > threshold
    assert weather_obj.check_temperature(threshold) == result


