var line_chart = function (data, selector) {
    var margin = {top: 20, right: 80, bottom: 30, left: 50},
        width = 940 - margin.left - margin.right,
        height = 500 - margin.top - margin.bottom;

    var parseDate = d3.time.format("%Y%m%d").parse;

    var x = d3.time.scale()
        .range([0, width]);

    var y = d3.scale.linear()
        .range([height, 0]);

    var color = d3.scale.category10();

    var xAxis = d3.svg.axis()
        .scale(x)
        .orient("bottom");

    var yAxis = d3.svg.axis()
        .scale(y)
        .orient("left");

    var line = d3.svg.line()
        .interpolate("basis")
        .x(function(d) { return x(d.date); })
        .y(function(d) { return y(d.count); });

    var svg = d3.select(selector).append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  color.domain(d3.keys(data[0]).filter(function(key) { return key !== "date"; }));

  data.forEach(function(d) {
    d.date = parseDate(d.date);
    });

    var revs = color.domain().map(function(name) {
        return {
          name: name,
          values: data.map(function(d) {
            return {date: d.date, count: +d[name]};
          })
        };
    });

    x.domain(d3.extent(data, function(d) { return d.date; }));

    y.domain([
        d3.min(revs, function(c) { return d3.min(c.values, function(v) { return v.count; }); }),
        d3.max(revs, function(c) { return d3.max(c.values, function(v) { return v.count; }); })
    ]);

    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);

    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis)
    .append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 6)
        .attr("dy", ".71em")
        .style("text-anchor", "end")
        .text("Number of revisions");

    var city = svg.selectAll(".city")
        .data(revs.slice().reverse())
        .enter().append("g")
        .attr("class", "city");

    city.append("path")
        .attr("class", "line")
        .attr("d", function(d) { return line(d.values); })
        .style("stroke", function(d) { return color(d.name); });

    city.append("text")
        .datum(function(d) { return {name: d.name, value: d.values[d.values.length - 1]}; })
        .attr("transform", function(d) { return "translate(" + x(d.value.date) + "," + y(d.value.count) + ")"; })
        .attr("x", 3)
        .attr("dy", ".35em")
        .text(function(d) { return d.name; });

    var legend = svg.selectAll(".legend")
        .data(revs)
        .enter().append("g")
        .attr("class", "legend")
        .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });

    legend.append("rect")
        .attr("x", width - 18)
        .attr("width", 18)
        .attr("height", 18)
        .style("fill", function(d) { return color(d.name); });

    legend.append("text")
        .attr("x", width - 24)
        .attr("y", 9)
        .attr("dy", ".35em")
        .style("text-anchor", "end")
        .text(function(d) { return d.name; });
};

var spark_graph = function (data, selector) {
    var g_editors = d3.select(selector).append("svg:svg").attr("width", "350px").attr("height", "30").attr('style', 'padding:10px;');
    var sp_max = d3.max(data) + 50;
    var x = d3.scale.linear().domain([0, data.length]).range([0, 300]);
    var y = d3.scale.linear().domain([d3.min(data), sp_max]).range([0, 30]);
    var line = d3.svg.line()
    .x(function(d,i) { 
        return x(i); 
    })
    .y(function(d) { 
        return y(sp_max - d); 
    });
    g_editors.append("svg:path").attr("d", line(data)).attr("class", "line");
};
