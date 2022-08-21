---
---

<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
<style>

body{
    margin-top:20px;
}
.card-box {
    padding: 20px;
    border-radius: 3px;
    margin-bottom: 30px;
    background-color: #fff;
}
.search-result-box .tab-content {
    padding: 30px 30px 10px 30px;
    -webkit-box-shadow: none;
    box-shadow: none;
    -moz-box-shadow: none
}

.search-result-box .search-item {
    padding-bottom: 20px;
    border-bottom: 1px solid #e3eaef;
    margin-bottom: 20px
}
.text-success {
    color: #0acf97!important;
}
a {
    color: #007bff;
    text-decoration: none;
    background-color: transparent;
}
.btn-custom {
    background-color: #02c0ce;
    border-color: #02c0ce;
}

.btn-custom, .btn-danger, .btn-info, .btn-inverse, .btn-pink, .btn-primary, .btn-purple, .btn-success, .btn-warning {
    color: #fff!important;
}
</style>

</head>

<script type="text/javascript">
    function build_wiki_search_url(pattern) {
        var base_url = "https://en.wikipedia.org/w/api.php";
        var request_url = "?action=query&format=json&generator=prefixsearch&prop=pageprops|description|info&inprop=url&gpslimit=10&gpssearch=";
        var url = base_url + request_url + pattern;
        return url;
    }

   function setWikiSearchResults(pages) {
       var querySource = "Wikipedia";
       $("#home").val("");
       for (const page in pages) {
           var rowHTML = `
                                <div class="row">
                                    <div class="col-md-12">
                                        <div class="search-item">
                                            <h4 class="mb-1"><a href="${pages[page].canonicalurl}">${querySource} - ${pages[page].title}</a></h4>
                                            <div class="font-13 text-success mb-3">${pages[page].canonicalurl}</div>
                                            <p class="mb-0 text-muted">${pages[page].description}</p>
                                        </div>
                                        <div class="clearfix"></div>
                                    </div>
                                </div>
           `;
           $("#home").append(rowHTML);
       }
   }

    $(document).ready(function() {
        var queryDefaultText = "Mindful Search Query";
        $("#query").click(function(e) {
            e.preventDefault();
            if($("#query").val() == queryDefaultText) {
                $("#query").val("");
            }
        });
        $("#query").focusout(function(e) {
            e.preventDefault();
            if($("#query").val() == "") {
                $("#query").val(queryDefaultText);
            }
        });
        $(".btn").click(function(e) {
            e.preventDefault();
            console.log("Submit button clicked");
            var pattern = $("#query").val();
            var url = build_wiki_search_url(pattern);
            $.ajax( {
                type: "GET",
                url: url,
                dataType: 'jsonp',
                success: function(data) {
                    console.log(Object.values(data.query.pages));
                    setWikiSearchResults(Object.values(data.query.pages));
                },
                error: function(errorMessage) {
                    console.log("damnn");
                }
            });
        });
    })

</script>
<div class="content">
    <div class="container">
        <div class="row">
            <div class="col-lg-12">
                <div class="search-result-box card-box">
                    <div class="row">
                        <div class="col-md-8 offset-md-2">
                            <div class="pt-3 pb-4">
                                <div id = "search_header" class="mt-4 text-center">
                                    <h4>Mindful Search</h4>
                                </div>
                                <div class="input-group">
                                    <input type="text" id="query" name="" class="form-control" value="Mindful Search Query">
                                    <div class="input-group-append">
                                        <button type="button" class="btn waves-effect waves-light btn-custom"><i class="fa fa-search mr-1"></i> Search</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="tab-content">
                        <div class="tab-pane active" id="home">
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- end row -->
    </div>
    <!-- container -->
</div>
