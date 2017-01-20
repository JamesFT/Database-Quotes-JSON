#Database Quotes JSON
##JSON file with more than 5000+ famous quotes.

###Some example on how to work on this JSON quotes file

```javascript
//return array of all quotes with 12 words max
var filePath = "quotes.js";
$.getJSON(filePath).done(function (data) {
	return data.filter(function (o) {
		return o.quoteText.split(" ").length <= 12;
	});
});

//return array of all quotes of Buddha
var filePath = "quotes.js";
	$.getJSON(filePath).done(function (data) {
		return data.filter(function (o) {
			return o.quoteAuthor === "Buddha";
		});
	});
}
```