const tabList = document.querySelectorAll('.tab_menu .list li');
const contents = document.querySelectorAll('.tab_menu .cont_area .cont')
let activeCont = ''; // 현재 활성화 된 컨텐츠 (기본:#tab1 활성화)

for(var i = 0; i < tabList.length; i++){
  tabList[i].querySelector('.btn').addEventListener('click', function(e){
    e.preventDefault();
    for(var j = 0; j < tabList.length; j++){
      // 나머지 버튼 클래스 제거
      tabList[j].classList.remove('is_on');

      // 나머지 컨텐츠 display:none 처리
      contents[j].style.display = 'none';
    }

    // 버튼 관련 이벤트
    this.parentNode.classList.add('is_on');

    // 버튼 클릭시 컨텐츠 전환
    activeCont = this.getAttribute('href');
    document.querySelector(activeCont).style.display = 'block';
  });
}




const startSEl = document.getElementById("startS");
const stopSEl = document.getElementById("stopS");
const resetSEl = document.getElementById("resetS");

const timerSEl = document.getElementById("timerS");

let intervalS; // 값이 없음. 즉, false
let startTime = 0;

// 초기화 함수 
function initS() {
    startTime = 0;
    updateTimerS();
}

// 100 -> 1초 
// 6000 -> 1분 
function updateTimerS() {

    let minutes = Math.floor(startTime / 6000); // 초 / 60 -> 분!!
    let left_times = startTime % 6000
    let seconds = Math.floor(left_times / 100);
    let miliseconds = left_times % 100; 
    let formattedTime = `${minutes.toString().padStart(2, "0")}:${seconds
        .toString().padStart(2, "0")}:${miliseconds
            .toString()
            .padStart(2, "0")}`;

    // 남의 시간이 변경되는 코드....
    timerSEl.innerHTML = formattedTime;
}

function startTimerS() {
    // 기존 setInterval이 존재하면 제거하는 로직!!
    if (intervalS) {
    stopTimerS();
    }
    // interval = setInterval의 식별할 수 있는 index 반환 
    // setInterval: 특정 시간 단위로 어떤 함수를 계속 실행함!!!
    intervalS = setInterval(() => {
        startTime++; 
        updateTimerS();

        // 1분이 지나면 멈추자!!
        if (startTime === 6000) {
            clearInterval(intervalS);
            alert("over 1 minutes!!");
            // init();
        }

    }, 10); // 0.01초에 한번씩 함수실행!!
}

function stopTimerS() {
    clearInterval(intervalS);
}

function resetTimerS() {
    // 기존에 있는 setInterval를 제거 
    clearInterval(intervalS);
    // 데이터 및 화면 초기화
    initS();
}

startSEl.addEventListener("click", startTimerS);
stopSEl.addEventListener("click", stopTimerS);
resetSEl.addEventListener("click", resetTimerS);



/////////////////////////////////////////////////////////////////////////////////////

const startTEl = document.getElementById("startT"); // 버튼
const stopTEl = document.getElementById("stopT");   // 버튼
const resetTEl = document.getElementById("resetT"); // 버튼

const timerTEl = document.getElementById("timerT"); // p_tag

const initialTime = 3;
let intervalT; // 값이 없음. 즉, false
let timeLeft = initialTime; // 25분(1500초)

function updateTimerT() { // 값을 계속해서 변경
    let minutes = Math.floor(timeLeft / 60); // 초 / 60 -> 분!!
    let seconds = timeLeft % 60; // 초 % 60 -> 나눈값의 나머지는 초!!!
    let formattedTime = `${minutes.toString().padStart(2, "0")}:${seconds
        .toString().padStart(2, "0")}`;

    // 남의 시간이 변경되는 코드....
    timerTEl.innerHTML = formattedTime;
}

function startTimerT() {
    // 기존 setInterval이 존재하면 제거하는 로직!!
    if (intervalT) {
    stopTimerT();
    }
    // interval = setInterval의 식별할 수 있는 index 반환 
    // setInterval: 특정 시간 단위로 어떤 함수를 계속 실행함!!!
    intervalT = setInterval(() => { //특정 주기별로 실행되는 함수 -> 한번 실행 = 계속 실행
        timeLeft--; // 함수가 실행될때마다 하나씩 줄어듬..
        // updateTimer를 통해서 화면에 변경된 시간을 적용!!!
        updateTimerT();
        // 남은 시간이 0초가 되면, 더 이상 함수를 실행하지 않음!!
        if (timeLeft === 0) {
            resetTimerT();
            alert("Time's up!");
        }
    }, 1000); // 1초에 한번씩 함수실행!!
}

function stopTimerT() {
    clearInterval(intervalT); // set Interval을 멈추는 로직ㄴ
}

function resetTimerT() {
    // 기존에 있는 setInterval를 제거 
    stopTimerT();
    // 데이터 및 화면 초기화
    timeLeft = initialTime;
    updateTimerT();
}

startTEl.addEventListener("click", startTimerT);
stopTEl.addEventListener("click", stopTimerT);
resetTEl.addEventListener("click", resetTimerT);