<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Article history information</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <!-- Le styles -->
    <link href="http://tools.wmflabs.org/revisionstats/static/css/bootstrap.css" rel="stylesheet">
    <style>
      body {
        padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */
      }
      .axis path,
      .axis line {
        fill: none;
        stroke: #000;
        shape-rendering: crispEdges;
      }

      .x.axis path {
       display: none;
      }

      .line {
        fill: none;
        stroke: steelblue;
        stroke-width: 1.5px;
      }
      path {
        stroke: steelblue;
        stroke-width: 1.5;
        fill: none;
      }
    </style>
    <script src="http://tools.wmflabs.org/revisionstats/static/js/d3.js"></script>
    <script src="http://tools.wmflabs.org/revisionstats/static/app.js"></script>
    <!--<link href="http://toolserver.org/~slaporte/views/css/bootstrap-responsive.css" rel="stylesheet"> -->

    <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->

    <!-- Le fav and touch icons -->
  </head>

  <body>

    <div class="navbar navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </a>
          <a class="brand" href="#">Article history information</a>
          <div class="nav-collapse">
            <form class="navbar-search pull-left" method="get" action="http://tools.wmflabs.org/revisionstats/cgi-bin/rev/stats">
              <input type="text" class="search-query" placeholder="Article name" name="title">
            </form>
            <ul class="nav pull-right">
              <li><a href="https://github.com/slaporte/revisions">About</a></li>
              <li class="dropdown">
              <a href="#"
                    class="dropdown-toggle"
                    data-toggle="dropdown">
                    Language
                    <b class="caret"></b>
              </a>
              <ul class="dropdown-menu">
                <li><a href="#">English</a></li>
              </ul>
            </li>
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>

    <div class="container">

    %include

    </div> <!-- /container -->

    <!-- Le javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->

    <script src="http://tools.wmflabs.org/revisionstats/static/js/jquery.js"></script>
    <script src="http://tools.wmflabs.org/revisionstats/static/js/bootstrap-dropdown.js"></script>

