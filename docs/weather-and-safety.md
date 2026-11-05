# Weather and safety

When the roof may open, when it must close, and what closes it automatically.

!!! danger "When in doubt, close"
    The roof must be closed when the weather is bad. If you can't tell whether the
    conditions are safe, or the weather values are old or missing, close the roof and ask.

## Where to see the weather

!!! todo "TODO"
    Where observers see the current weather: GUI tab, the pyobs-weather web page
    (`http://ocs-server:8002/`, site network only), allsky camera images. Add a screenshot
    and say how to tell that a value is old.

Weather sources at the telescope:

| Source | Measures |
|---|---|
| Boltwood cloud sensor | Cloud (sky − ambient temperature), rain / wet. TODO: confirm once the sensor protocol is known. |
| Weather mast | Temperature, humidity, dew point, pressure (two sensors) |
| Allsky camera | Images of the whole sky |
| TODO | Wind? |

## Weather limits

!!! todo "TODO"
    The agreed limits for opening and for closing, and which sensor each one comes from.
    These are set in pyobs-weather. Write here who decided them and when.

| Quantity | Open only if | Close when | Source |
|---|---|---|---|
| Cloud (sky − ambient) | TODO | TODO | Boltwood |
| Rain | none | any | TODO |
| Humidity | TODO | TODO | TODO |
| Dew point margin | TODO | TODO | TODO |
| Wind | TODO | TODO | TODO |
| Sun altitude | TODO | TODO | — |

## Automatic closing

!!! todo "TODO"
    What closes the roof automatically (weather module, roof watchdog, power loss), and what
    does **not**. What happens when the network or `ocs-server` goes down while the roof is
    open.

## Safety on site

If you are at the telescope, read [Safety on site](maintenance/safety.md).
