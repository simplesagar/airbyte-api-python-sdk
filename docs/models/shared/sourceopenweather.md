# SourceOpenweather

The values required to configure the source.


## Fields

| Field                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `appid`                                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                     | Your OpenWeather API Key. See <a href="https://openweathermap.org/api">here</a>. The key is case sensitive.                                                                                                                            |                                                                                                                                                                                                                                        |
| `lang`                                                                                                                                                                                                                                 | [Optional[SourceOpenweatherLanguage]](../../models/shared/sourceopenweatherlanguage.md)                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                     | You can use lang parameter to get the output in your language. The contents of the description field will be translated. See <a href="https://openweathermap.org/api/one-call-api#multi">here</a> for the list of supported languages. | en                                                                                                                                                                                                                                     |
| `lat`                                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                     | Latitude for which you want to get weather condition from. (min -90, max 90)                                                                                                                                                           | 45.7603                                                                                                                                                                                                                                |
| `lon`                                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                                                     | Longitude for which you want to get weather condition from. (min -180, max 180)                                                                                                                                                        | 4.835659                                                                                                                                                                                                                               |
| `source_type`                                                                                                                                                                                                                          | [SourceOpenweatherOpenweather](../../models/shared/sourceopenweatheropenweather.md)                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                     | N/A                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                        |
| `units`                                                                                                                                                                                                                                | [Optional[SourceOpenweatherUnits]](../../models/shared/sourceopenweatherunits.md)                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                     | Units of measurement. standard, metric and imperial units are available. If you do not use the units parameter, standard units will be applied by default.                                                                             | standard                                                                                                                                                                                                                               |