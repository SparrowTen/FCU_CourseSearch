let hero = document.querySelector(".hero");
let slider = document.querySelector(".slider");
let animation = document.querySelector("section.animation-wrapper");

const time_line = new TimelineMax();

// parameter1 是要控制的對象
// parameter2 是duration
// parameter3 是控制對象的原始狀態
// parameter4 是控制對象的動畫結束後的狀態
// parameter5
time_line
  .fromTo(
    hero,
    1.5,
    { height: "0vh", width: "0vw" },
    { height: "40vh", width: "26vw", ease: Power2.easeInOut }
  )
  .fromTo(
    slider,
    1,
    { x: "-100%" },
    { x: "0%", ease: Power2.easeInOut },
    "-=1.2"
  )
  .fromTo(
    animation,
    0.3,
    { opacity: 1, zIndex: 500 },
    { opacity: 0, zIndex: -500 }
  );
