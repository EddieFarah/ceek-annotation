$(function() {

        $(".modal").show();
        //get company names
        $.ajax({
                type: "GET",
                url: "/ceek/job_offers/retrieve/list/",
                dataType: "json",
                success: function(data){
                    results = data['result'];
                    generate_list(results)

                }
        });

        function generate_list(results)
        {
            //company names
            var arr_company_names= [];
            $.each(results, function(index, element){
                resultelem = element;
                var company= resultelem['company'];
                arr_company_names.push(company);
            });
            arr_company_names.sort();
            var company_uniqueNames = [];
            $.each(arr_company_names, function(i, el){
                if($.inArray(el, company_uniqueNames) === -1) company_uniqueNames.push(el);
            });
            var companies_select = document.getElementById("companies_select");
            $.each(company_uniqueNames, function(index, company) {
                var el = document.createElement("option");
                el.textContent = company;
                el.value = company;
                companies_select.appendChild(el);
            });

            //company locations
            var arr_company_locations= [];
            $.each(results, function(index, element){
                resultelem = element;
                var location= resultelem['location'];
                arr_company_locations.push(location);
            });
            arr_company_locations.sort();
            var location_uniqueNames = [];
            $.each(arr_company_locations, function(i, el){
                if($.inArray(el, location_uniqueNames) === -1) location_uniqueNames.push(el);
            });
            var locations_select = document.getElementById("locations_select");
            $.each(location_uniqueNames, function(index, location) {
                var el = document.createElement("option");
                el.textContent = location;
                el.value = location;
                locations_select.appendChild(el);
            });

            //company positions
            var arr_company_positions= [];
            $.each(results, function(index, element){
                resultelem = element;
                var position= resultelem['title'];
                arr_company_positions.push(position);
            });
            arr_company_positions.sort();
            var positions_uniqueNames = [];
            $.each(arr_company_positions, function(i, el){
                if($.inArray(el, positions_uniqueNames) === -1) positions_uniqueNames.push(el);
            });
            var positions_select = document.getElementById("positions_select");
            $.each(positions_uniqueNames, function(index, position) {
                var el = document.createElement("option");
                el.textContent = position;
                el.value = position;
                positions_select.appendChild(el);
            });

             var list = "<ul>";

            results_copy = results
             $.each(results, function(index, element) {

                 resultelem = element;

                 var id= resultelem['id'];
                 var title= resultelem['title'];
                 var description= resultelem['description'];
                 var compnay_url= resultelem['compnay_url'];
                 var created_at= resultelem['created_at'];
                 var company= resultelem['company'];
                 var how_to_apply= resultelem['how_to_apply'];
                 var location= resultelem['location'];
                 var url= resultelem['url'];
                 var type= resultelem['type'];

                 var compnay_logo= resultelem['compnay_logo'];
                 if(!compnay_logo)
                      compnay_logo = "http://github-jobs.s3.amazonaws.com/aa9eed70-71cd-11e5-8978-1cefa7cbc255.png"
                 else if (compnay_logo == "chrome-extension://fomgcolbgdjbmnabgijnbmmmoimhlidi/images/logo.png")
                      compnay_logo = "http://github-jobs.s3.amazonaws.com/aa9eed70-71cd-11e5-8978-1cefa7cbc255.png"

                 list +=`<li id=`+id+`name=`+id+`>
                        <div class="container" >
                            <ul class="list-group">
                                <li>
                                    <div class="panel panel-default">
                                        <div class="panel-body">
                                            <div class="panel-more1">
                                                <img height="75" width="75" src="`+compnay_logo+`" /><br />
                                                <div style="text-align: center;">
                                                    <span >
                                                        `+ company +`
                                                    </span>
                                                </div>
                                            </div>
                                            <div class="panel-info">
                                                <p><strong>`+ title +`</strong></p>
                                                <p><strong>`+ location+`</strong></p>
                                                <div class="bs-example">

                                                </div>
                                            </div>
                                            <div class="panel-group" id="accordion" style="margin-top:100px;float: center;">
                                                        <div class="panel panel-default" style="margin-top:10px;">
                                                            <div class="panel-heading" style="text-align: center;">
                                                                <h4 class="panel-title">
                                                                <a data-toggle="collapse" data-parent="#accordion" href=#collapse-`+id+`>Job Description</a>
                                                                </h4>
                                                            </div>
                                                            <div id=collapse-`+id+` class="panel-collapse collapse" style="padding:5px;" aria-expanded="false">
                                                            `+description+`
                                                            </div>
                                                        </div>
                                            </div>
                                            <div class="panel-rating" style="margin-top:10px;float: right;" >
                                                <font size="2">Created at: `+ created_at +`</font>
                                            </div>
                                        </div>
                                    </div>
                                </li>
                            </ul>
                        </div>
                 </li>`;
             });


             list +="</ul>";
             document.getElementById("chart_div").innerHTML=list;
             $(".modal").hide();
        }

        //------------------------------------ Filter Button---------------------------------------------------
        $('#filterButton').click(function(){
            $(".modal").show();

            var company = $("#companies_select").val();
            var location = $("#locations_select").val();
            var position = $("#positions_select").val();

            $.ajax({
                type: "POST",
                url: "/ceek/job_offers/filter/",
                data: { "company" : company , "location" : location, "position" : position},
                dataType: "json",
                success: function(data){
                    results = data['result'];
                    generate_list(results);
                    $(".modal").hide();
                }
            });
        });

        //------------------------------------ Load Data Button---------------------------------------------------
        $('#loadButton').click(function(){
            $(".modal").show();

            $.ajax({
                type: "GET",
                url: "/ceek/job_offers/list/",
                dataType: "json",
                success: function(data){
                    results = data['result'];
                    $(".modal").hide();
                }
            });
        });



        //------------------------------------ CompareButton End--------------------------------------------------------
        $(document).on('click', '.navbar-nav li', function() {
           $(".navbar-nav li").removeClass("active");
           $(this).addClass("active");
        });
        });
