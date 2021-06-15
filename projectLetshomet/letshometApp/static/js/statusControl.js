function popupcontent(title, n) {
  //첫번째 현황관리 버튼을 누르면 percent바뀌고 팝업창 제목 바낌.
  var popup_title = document.querySelector(".popup-title");
  popup_title.innerHTML = title;
  if (n == 1) {
    var div_percentage = document.getElementById("percent1");
    var figure = document.getElementById("complete_percentage");
    div_percentage.style.width = figure.innerHTML + "%";
    div_percentage.innerHTML = figure.innerHTML + "%";
  }
}
