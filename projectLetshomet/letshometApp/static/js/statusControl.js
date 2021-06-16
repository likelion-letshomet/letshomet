function popupcontent(title) {
  //첫번째 현황관리 버튼을 누르면 percent바뀌고 팝업창 제목 바낌.
  var popup_title = document.querySelector(".popup-title");
  popup_title.innerHTML = title;
}
let homet_status_LS1 = [];

const homet_LS_key1 = "hometStatus1";
const homet_LS_key2 = "hometStatus2";
const homet_LS_key3 = "hometStatus3";
function init() {
  const savecheck_btn = document.querySelector(".save_btn");
  const pop_title = document.querySelectorAll(
    ".user_challenge_check_content_title"
  );

  const btn1 = document.querySelector("#status_btn1");
  const btn2 = document.querySelector("#status_btn2");
  const btn3 = document.querySelector("#status_btn3");

  var nth = 0;

  btn1.addEventListener("click", function () {
    var title = pop_title[0].innerText;
    console.log(title);
    console.log("init 함수");
    nth = 1;
    $("input:checkbox[name=check]").prop("checked", false); // 전체해제하기
    $("input:radio[name=week]").prop("checked", false); // 전체해제하기
    load(title, nth);
  });
  btn2.addEventListener("click", function () {
    var title = pop_title[1].innerText;
    console.log(title);
    console.log("init 함수");
    nth = 2;
    $("input:checkbox[name=check]").prop("checked", false); // 전체해제하기
    $("input:radio[name=week]").prop("checked", false); // 전체해제하기
    load(title, nth);
  });
  btn3.addEventListener("click", function () {
    var title = pop_title[2].innerText;
    console.log(title);
    console.log("init 함수");
    nth = 3;
    $("input:checkbox[name=check]").prop("checked", false); // 전체해제하기
    $("input:radio[name=week]").prop("checked", false); // 전체해제하기
    load(title, nth);
  });

  //savecheck_btn.addEventListener("click", handleSubmit(homet_LS_key, title));
  savecheck_btn.addEventListener("click", function (e) {
    // 전체삭제

    handleSubmit(pop_title[nth - 1].innerText, nth);
  });
  //
}
function saveStatus(checkedweek, daycheck, title, nth) {
  const statusObj = {
    title: title,
    week: checkedweek,
    days: daycheck,
  };
  if (nth === 1) {
    homet_status_LS1.push(statusObj);
    localStorage.setItem(homet_LS_key1, JSON.stringify(homet_status_LS1));
  } else if (nth === 2) {
    homet_status_LS1.push(statusObj);
    localStorage.setItem(homet_LS_key2, JSON.stringify(homet_status_LS1));
  } else {
    homet_status_LS1.push(statusObj);
    localStorage.setItem(homet_LS_key3, JSON.stringify(homet_status_LS1));
  }
  //이미 있는 title 일 때만

  homet_status_LS1 = [];
  console.log("save 함수");
}
function paint(checkedweek, daycheck, title) {
  if (checkedweek > 0) {
    console.log("paing 함수");
    $("input:radio[name=week]")[checkedweek - 1].click();
    $("input:radio[name=week]")[checkedweek - 1].checked = true;
    for (var i = 0; i < daycheck; i++) {
      $("input:checkbox[name=check]")[i].checked = true;
    }
  }
  if (checkedweek === 0) {
    $("input:checkbox[name=check]").prop("checked", false); // 전체해제하기
  }
  if (daycheck === 0) {
    $("input:radio[name=week]").prop("checked", false); // 전체해제하기
  }
}

function handleSubmit(title, nth) {
  console.log("handle함수");
  if ($("input:radio[name=week]:checked")) {
    var checkedweek = $("input:radio[name=week]:checked").val();
    checkedweek = parseInt(checkedweek);
  }
  const daycheck = $("input:checkbox[name=check]:checked").length;
  saveStatus(checkedweek, daycheck, title, nth);
}
function paint_percent(week, days, nth) {
  var complete_percent = (days / (week * 7)) * 100;
  complete_percent = Math.round(complete_percent);
  console.log(complete_percent + "%");

  var div_percentage = document.getElementById("percent" + nth);

  var figure = document.getElementById("complete_percentage");
  figure.innerHTML = complete_percent + "% 완주!!";
  var figure_percent = complete_percent;
  div_percentage.style.width = figure_percent + "%";
  div_percentage.innerHTML = figure_percent + "%";
}
function load(title, nth) {
  var loadedstatus = localStorage.getItem(homet_LS_key1);
  if (nth === 1) {
    loadedstatus = localStorage.getItem(homet_LS_key1);
  } else if (nth === 2) {
    loadedstatus = localStorage.getItem(homet_LS_key2);
  } else {
    loadedstatus = localStorage.getItem(homet_LS_key3);
  }

  if (loadedstatus !== null) {
    const parsed = JSON.parse(loadedstatus);
    parsed.forEach(function (status) {
      if (status.title === title) {
        paint(status.week, status.days, title);
        paint_percent(status.week, status.days, nth); /////////////////
      } else {
        paint(0, 0, title); /////////////////
      }
    });
  }
}
init();
