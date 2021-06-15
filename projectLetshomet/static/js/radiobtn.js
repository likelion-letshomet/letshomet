$(document).ready(function () {
  $("input:radio[name=week]").click(function () {
    if ($(this).checked) {
      $("input:radio[name=week]").attr("checked", false);

      $(this).checked = true;
    }
    /*윗부분: 라디오 버튼이 4개 이상일 때 하나만 선택이 되도록 한다.*/
    if ($("input:radio[name=week]:checked")) {
      var week = $("input:radio[name=week]:checked").val();
      week = parseInt(week);
      console.log(week);
      $(".status-check").remove();
      for (var a = 0; a < week; a++) {
        $(".popup-content-status-choose").append(
          '<div class="status-check"></div>'
        );
      }

      var checkbox = document.querySelectorAll(".status-check");
      var checknum = 0;
      for (var k = 0; k < checkbox.length; k++) {
        k = k + 1;
        for (var i = 1; i <= 7; i++) {
          checknum++;

          $(".status-check:nth-child(" + k + ")").append(
            '<div><input type="checkbox" class="check' +
              checknum +
              '" name="check" />' +
              i +
              "</div>"
          );
        }
        k = k - 1;
      }
    }
  });
});
