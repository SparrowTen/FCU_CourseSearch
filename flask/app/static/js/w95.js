/*!

=========================================================
* Pixel Bootstrap 4 UI Kit
=========================================================

* Product Page: http://pixel.themesberg.com
* Copyright 2018 Themesberg (https://www.themesberg.com)

* Coded by themesberg.com

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
$(".Schedule").hide();
$(document).ready(function () {
  // Tooltip
  $('[data-toggle="tooltip"]').tooltip();

  // Popover
  $('[data-toggle="popover"]').each(function () {
    var popoverClass = "";
    if ($(this).data("color")) {
      popoverClass = "popover-" + $(this).data("color");
    }
    $(this).popover({
      trigger: "focus",
      template:
        '<div class="popover ' +
        popoverClass +
        '" role="tooltip"><div class="arrow"></div><h3 class="popover-header"></h3><div class="popover-body"></div></div>',
    });
  });

  // Additional .focus class on form-groups
  $(".form-control")
    .on("focus blur", function (e) {
      $(this)
        .parents(".form-group")
        .toggleClass("focused", e.type === "focus" || this.value.length > 0);
    })
    .trigger("blur");

  // When in viewport
  $('[data-toggle="on-screen"]')[0] &&
    $('[data-toggle="on-screen"]').onScreen({
      container: window,
      direction: "vertical",
      doIn: function () {
        //alert();
      },
      doOut: function () {
        // Do something to the matched elements as they get off scren
      },
      tolerance: 200,
      throttle: 50,
      toggleClass: "on-screen",
      debug: false,
    });

  // Scroll to anchor with scroll animation
  $('[data-toggle="scroll"]').on("click", function (event) {
    var hash = $(this).attr("href");
    var offset = $(this).data("offset") ? $(this).data("offset") : 0;

    // Animate scroll to the selected section
    $("html, body")
      .stop(true, true)
      .animate(
        {
          scrollTop: $(hash).offset().top - offset,
        },
        600
      );

    event.preventDefault();
  });

  function formatAMPM(date) {
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var ampm = hours >= 12 ? "pm" : "am";
    hours = hours % 12;
    hours = hours ? hours : 12; // the hour '0' should be '12'
    minutes = minutes < 10 ? "0" + minutes : minutes;
    var strTime = hours + ":" + minutes + " " + ampm;
    return strTime;
  }

  $(".time").text(formatAMPM(new Date()));

  // copy docs
  $(".copy-docs").on("click", function () {
    var $copy = $(this);
    var htmlEntities = $copy
      .parents(".nav-wrapper")
      .siblings(".card")
      .find(".tab-pane:last-of-type")
      .html();
    var htmlDecoded = $("<div/>").html(htmlEntities).text().trim();

    var $temp = $("<textarea>");
    $("body").append($temp);
    $temp.val(htmlDecoded).select();
    document.execCommand("copy");
    $temp.remove();

    $copy.text("Copied!");
    $copy.addClass("copied");

    setTimeout(function () {
      $copy.text("Copy");
      $copy.removeClass("copied");
    }, 1000);
  });

  $(".buttonschedule").click(function () {
    // $(".Schedule").show();
    $(".Schedule").fadeToggle();
    console.log("show");
  });

  $(".closeschedule").click(function () {
    $(".Schedule").fadeOut();
    // $(".Schedule").hide();
    console.log("hide");
  });

  $(".closeschedule").click(function () {
    $(".Schedule").fadeOut();
    // $(".Schedule").hide();
    console.log("hide");
  });

  $("div.tg").hide();
  $("div.result").hide();

  //remove the "Copying Files ..." window after the user clicks on the "Cancel" button and stop the alert pop up function
  var i = 0;
  $("button").on("click", function () {
    $(".window").fadeOut();
    an.stop();
    $("div.result").fadeIn();
  });

  //automaticaly remove the "Copying Files ..." window after the alert pop up
  var an = $("div.rect .a").animate({ width: "100%" }, 1000, function () {
    $(".window").fadeOut();
    $("div.result").fadeIn();
  });

  /*change the the pourcentage color from black to white at 50%
    stop the incrementation when the pourcentage reach 100%
    */
  var clr = setInterval(function () {
    $(".prct").text(i++ + "%");
    if (i == 50) {
      $(".prct").css({ color: "white" });
    }

    if (i == 101) {
      clearInterval(clr);
    }
  }, 10);

  //generates the current time
  var d = new Date();
  var mins = ("0" + d.getMinutes()).slice(-2);
  $("div.time").text(d.getHours() + ":" + mins);

  //show and hide the start menu
  $("div.wnds").on("click", function () {
    $("div.tg").fadeToggle(50);
  });

  var count = 1;
  $("#std_degree").on("change", function () {
    count = 1;
    $("#std_degree option:selected").each(function () {
      // console.log($(this).val());
      $.get(
        "http://127.0.0.1:5000/API/Id/getDept?degree=" + $(this).val(),
        function (data, status) {
          // console.log(data);
          var list = "<option>學院</option>";

          for (var d in data) {
            list +=
              "<option value=" +
              data[d].dept_id +
              ">" +
              data[d].dept_name +
              "</option>";
          }
          $("#std_dept").html(list);
          count++;
        }
      );
    });
  });

  $("#std_dept").on("change", function () {
    if (count != 2) {
      window.location.reload();
      count = 1;
    }
    $("#std_dept option:selected").each(function () {
      // console.log($(this).val());
      $.get(
        "http://127.0.0.1:5000/API/Id/getUnit?dept_id=" + $(this).val(),
        function (data, status) {
          console.log(data);
          var list = "<option>系所</option>";

          for (var d in data) {
            list +=
              "<option value=" +
              data[d].unit_id +
              ">" +
              data[d].unit_name +
              "</option>";
          }
          $("#std_unit").html(list);
          count++;
        }
      );
    });
  });

  $("#std_unit").on("change", function () {
    if (count != 3) {
      window.location.reload();
      count = 1;
    }
    $("#std_unit option:selected").each(function () {
      // console.log($(this).val());
      $.get(
        "http://127.0.0.1:5000/API/Id/getClass?unit_id=" + $(this).val(),
        function (data, status) {
          console.log(data);
          var list = "<option>班級</option>";

          for (var d in data) {
            list +=
              "<option value=" +
              data[d].cls_id +
              ">" +
              data[d].cls_name +
              "</option>";
          }
          $("#std_cls").html(list);
        }
      );
    });
  });
});
