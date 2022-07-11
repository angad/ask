# Mindful Search

<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
</head>

<script type="text/javascript">
	function build_wiki_search_url(pattern) {
		var base_url = "https://en.wikipedia.org/w/api.php";
		var request_url = "?action=query&format=json&generator=prefixsearch&prop=pageprops|description|info&inprop=url&gpslimit=1&gpssearch=";
		var url = base_url + request_url + pattern;
		return url;
	}

	$(document).ready(function() {
		$("search").click(function(e) {
			e.preventDefault();
			console.log("Submit button clicked");
			var pattern = $("#query").val();
			var url = build_wiki_search_url(pattern);
			$.ajax( {
				type: "GET",
				url: url,
				dataType: 'jsonp',
				success: function(data) {
					console.log(data.query.searchinfo.totalhits);
				},
				error: function(errorMessage) {
					console.log("damnn");
				}
			});
		});
	})

</script>
<center>
<input type ="text" size="20" id="query"/>
<button id="search">Search</button>
</center>
