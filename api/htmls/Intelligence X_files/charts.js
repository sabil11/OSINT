function createHeatmap(el, data, type) {
  var selectedDate = el.parent().attr('data-date');

  var years = d3.nest()
      .key(function(d) { return d.date.getUTCFullYear(); })
    .entries(data)
    .reverse();

  var cellSize = 13;
  var weekday = "sunday";
  var height = cellSize * (weekday === "weekday" ? 7 : 9)
  var timeWeek = weekday === "sunday" ? d3.utcSunday : d3.utcMonday
  var countDay = weekday === "sunday" ? function(d) { return d.getUTCDay(); } : function(d) { (d.getUTCDay() + 6) % 7; };

  function pathMonth(t) {
    var n = weekday === "weekday" ? 5 : 7;
    var d = Math.max(0, Math.min(n, countDay(t)));
    var w = timeWeek.count(d3.utcYear(t), t);
    if ( d === 0 ) {
      return 'M' + w * cellSize + ',0V' + n * cellSize;
    } else if ( d === n ) {
      return 'M' + (w + 1) * cellSize + ',0V' + n * cellSize;
    } else {
      return 'M' + (w + 1) * cellSize + ',0V' + d * cellSize + 'H' + w * cellSize + 'V' + n * cellSize;
    }
  }

  var formatDate = d3.utcFormat("%d.%m.%Y");

  var formatDay = function(d) { return "SMTWTFS"[d.getUTCDay()]; };

  var formatMonth = d3.utcFormat("%b");

  var formatTooltip = d3.utcFormat('%A %B %d, %Y');

  var color = d3.scaleLinear()
    .domain([0, 1, 25])
    .range(['#EEEEEE', '#CCCCFF', '#007bff'])
    .interpolate(d3.interpolateRgb);

  var svg = d3.select(el[0]);
  el.css({ 'font-size': '12px', width: cellSize * 53 + 50 + 'px', height: height});

  var year = svg.selectAll("g")
    .data(years)
    .join("g")
      .attr("transform", function(d, i) { return 'translate(40,' + height * i + cellSize * 1.5 +')'; });

  year.append("text")
      .attr("x", -5)
      .attr("y", -6)
      .attr("font-weight", "bold")
      .attr("text-anchor", "end")
      .attr("fill", "#fff")
      .text(function(d) { return d.key; });

  year.append("g")
      .attr("text-anchor", "end")
    .selectAll("text")
    .data((weekday === "weekday" ? d3.range(2, 7) : d3.range(7)).map(function(i) { return new Date(1995, 0, i);}))
    .join("text")
      .attr("x", -5)
      .attr("y", function(d) { return (countDay(d) + 0.5) * cellSize; })
      .attr("fill", "#fff")
      .text(formatDay);

  var tooltip = $('#chartTooltip');
  if ( tooltip.length <= 0 ) {
    tooltip = $('<div id="chartTooltip" style="height: 46px; opacity: 0;"></div>');

    el.parent().append(tooltip);
  }

  var dateEl = null;

  year.append("g")
    .selectAll("rect")
    .data(function(d) { return d.values; })
    .join("rect")
      .attr("width", cellSize - 1)
      .attr("height", cellSize - 1)
      .attr("x", function(d) { return timeWeek.count(d3.utcYear(d.date), d.date) * cellSize + 0.5; })
      .attr("y", function(d) { return countDay(d.date) * cellSize + 0.5; })
      .attr("fill", function(d) {
        if ( d.selector == selectedDate ) {
          dateEl = $(this);
          return 'red';
        } else {
          return color(d.value);
        }
      })
      .attr('stroke', 'black')
      .attr('stroke-opacity', '0')
    .on("mouseover", function(d) {
      $(this).attr('stroke-opacity', '0.8')
      var textHelper = d.value == 1 ? ' document on ' : ' documents on ';
      tooltip.html(d.value + textHelper + formatTooltip(d.date))
        .css("opacity", .9)
        .css("left", (d3.event.pageX - 60  + "px"))
        .css("top", (d3.event.pageY - 50 + $('#stats_chart').scrollTop()) + "px");
    })
    .on("mouseout", function(d) {
      $(this).attr('stroke-opacity', '0');
      tooltip.css("opacity", 0);
    })
    .on("click", function(d) {
      var element = el.parent();
      if ( element.hasClass('activeFilter') ) {
        var existingDate = new Date(element.attr('data-date'));
        if ( new Date(d.selector).getTime() == existingDate.getTime() ) {
          element.removeClass('activeFilter');
          element.removeAttr('data-type');
          element.removeAttr('data-date');
          $(this).attr("fill", color(d.value));
          dateEl = null;
        } else {
          if ( !! dateEl ) {
            dateEl.attr('fill', color(d.value));
          }
          element.attr('data-date', d.selector);
          dateEl = $(this);
          $(this).attr('fill', 'red');
        }
      } else {
        element.addClass('activeFilter');
        element.attr('data-type', type);
        element.attr('data-date', d.selector);
        $(this).attr('fill', 'red');
        dateEl = $(this);
      }
      kleissner.frontendChanges.onToggleFilter();
    });

  var month = year.append("g")
    .selectAll("g")
    .data(function(d) {
      return d3.utcMonths(d3.utcMonth(new Date(d.values[0].date.getUTCFullYear(), 1, 1)), new Date(d.values[d.values.length - 1].date.getUTCFullYear(), 12, 1));
    })
    .join("g");

  month.filter(function(d, i) { return i; }).append("path")
      .attr("fill", "none")
      .attr("stroke", "#000")
      .attr("stroke-width", 2)
      .attr("d", pathMonth);

  month.append("text")
      .attr("x", function(d) { return timeWeek.count(d3.utcYear(d), timeWeek.ceil(d)) * cellSize + 2; })
      .attr("y", -5)
      .attr("fill", "#fff")
      .text(formatMonth);
}

function createPieChart(el, data, type, width) {
  var total = 0;
  for ( var i = 0; i < data.length; i++ ) {
    total += data[i].value;
  }

  var width = width;

  var pie = d3.pie()
    .sort(null)
    .value(function(d) { return d.value; });

  var arc = d3.arc().innerRadius(0).outerRadius(width / 2 - 1);

  var radius = width / 2 * 0.8;
  var arcLabel = d3.arc().innerRadius(radius).outerRadius(radius);

  var color = d3.scaleOrdinal()
    .domain(data.map(function(d) { return d.name; }))
    .range(d3.quantize(function(t) { return d3.interpolateSpectral(t * 0.8 + 0.1); }, data.length).reverse());

  var arcs = pie(data);

  var svg = d3.select(el[0])
    .attr("text-anchor", "middle");

  el.css({ 'font-size': '12px', width: width, height: width});

  var g = svg.append("g")
    .attr("transform", 'translate(' + width / 2 + ', ' + width / 2 + ')');

  g.selectAll("path")
    .data(arcs)
    .enter().append("path")
      .attr("fill", function(d) { return color(d.data.name); })
      .attr("d", arc);

  var text = g.selectAll("text")
    .data(arcs)
    .enter().append("text")
      .attr("transform", function(d) { return 'translate(' + arcLabel.centroid(d) + ')'; })
      .attr("dy", "0.35em");

  /*text.append("tspan")
    .attr("x", 0)
    .attr("y", "-0.7em")
    .style("font-weight", "bold")
    .text(function(d) { return d.data.name; });

  text.append("tspan")
    .attr("x", 0)
    .attr("y", "0.7em")
    .attr("fill-opacity", 0.7)
    .text(function(d) {
      return Math.round(d.data.value/total * 10000) / 100 + '%';
    });*/

  var legendDiv = $('<div class="chartLegend" style="display:flex;flex-direction:column;justify-content:center;font-size:14px;padding:0;margin-left: 20px;"></div>');
  for ( var i = 0; i < data.length; i++ ) {
    var classFilter = data[i].filter == true ? ' activeFilter' : '';
    var legendDivRow = $('<div class="legendRow'+classFilter+'" data-type="' + type + '" data-value="' + data[i].selector + '"><div style="display: inline-block;width: 10px; height: 10px; margin-right: 10px; background-color: ' + color(data[i].name) + '"></div>' + data[i].name + ': ' + data[i].value + ' (' + Math.round(data[i].value/total * 10000) / 100 + '%)' + '</div>');
    legendDivRow.on('click', kleissner.frontendChanges.onToggleFilter);
    legendDiv.append(legendDivRow);
  }
  el.parent().append(legendDiv);
}

function createBarChart(el, data, width, height) {
  var svg = d3.select(el[0]);

  el.css({ width: width, height: height});
  var margin = ({top: 20, right: 0, bottom: 30, left: 40})

  var x = d3.scaleBand()
    .domain(data.map(function(d) { return d.name; }))
    .range([margin.left, width - margin.right])
    .padding(0.1)

  var y = d3.scaleLinear()
    .domain([0, d3.max(data, function(d) { return d.value;} )]).nice()
    .range([height - margin.bottom, margin.top])

  var xAxis = function (g) {
    g.attr("transform", 'translate(0, ' + (height - margin.bottom) + ')')
      .call(d3.axisBottom(x).tickSizeOuter(0));
  };

  var yAxis = function (g) {
    g.attr("transform", 'translate(' + margin.left + ', 0)')
      .call(d3.axisLeft(y))
      .call(function(g) { return g.select(".domain").remove(); });
  };

  svg.append("g")
      .attr("fill", "steelblue")
    .selectAll("rect")
    .data(data)
    .join("rect")
      .attr("x", function(d) { return x(d.name); })
      .attr("y", function(d) { return y(d.value); })
      .attr("height", function(d) { return y(0) - y(d.value); })
      .attr("width", x.bandwidth());

  svg.append("g")
    .call(xAxis);

  svg.append("g")
    .call(yAxis);

  var legendDiv = $('<div class="chartLegend" style="display:flex;flex-direction:column;justify-content:center;font-size:14px;padding:0;margin-left: 20px;"></div>')
  for ( var i = 0; i < data.length; i++ ) {
    legendDiv.append('<div>' + data[i].name + ': ' + data[i].value + '</div>')
  }
  el.parent().append(legendDiv);
}
