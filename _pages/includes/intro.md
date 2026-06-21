
# 👋 About me
Hi! I'm Junlin Liu, a graduate student majoring in Artificial Intelligence at **[<img src="../images/casia.svg" alt="icon" style="height:25px; vertical-align:middle;">Institute of Automation Chinese Academy of Sciences (CASIA)](http://www.ia.cas.cn/)**, and **[<img src="../images/ucas.svg" alt="icon" style="height:25px; vertical-align:middle;">University of Chinese Academy of Sciences (UCAS)](https://www.ucas.ac.cn/)**.

I’m currently a research intern focusing on Agentic RL and Agent Self-Evolution at [**<img src="../images/qwen.svg" alt="icon" style="height:22px; vertical-align:middle;">Alibaba Qwen MOS Lab**](https://github.com/Qwen-Applications). Previously, I held research intern positions at [**<img src="../images/longcat.svg" alt="icon" style="height:23px; vertical-align:middle;">Meituan LongCat Team**](https://github.com/meituan-longcat), [**<img src="../images/wenxin.svg" alt="icon" style="height:22px; vertical-align:middle;">Baidu Ernie Team**](https://github.com/ernie-research) and [**<img src="../images/x-humanoid.svg" alt="icon" style="height:25px; vertical-align:middle;">X-Humanoid LLM Team**](https://github.com/Open-X-Humanoid). 


<!-- 
My research interests include Reinforcement Learning, Large Language Models and Multi-Agent Cooperation and Games. I am particularly interested in evaluating and improving the reasoning capabilities of foundation models, with a focus on challenging mathematical and general reasoning. 
-->

**Research Interests：**
- **🧬 Self-Evolving Agent** — Building adaptive autonomous agents that continuously improve through RL and agent–environment co-evolution.
- **🤖 Agentic Reinforcement Learning** — Training general agent intelligence via fundamental RL-based optimization.
- **🔬 LLM Evaluation and Benchmark** — Evaluating and improving the reasoning capabilities of foundation models. 



💬 Please feel free to add me on WeChat: [**AaronLiu0702**](../../images/wx.png).


# 🎈 Activities

<style>
.activities-scroll {
  max-height: 320px; overflow-y: auto; padding: 8px 6px;
  border: 1px solid #eaeaea; border-radius: 12px; background: #fff;
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.6), 0 6px 14px rgba(0,0,0,0.04);
}
.activities-scroll::-webkit-scrollbar { width: 8px; }
.activities-scroll::-webkit-scrollbar-thumb { background: #ddd; border-radius: 4px; }
.activities-container { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 15px; }
.activities-item { flex: 0 0 calc(32.5% - 10px); text-align: center; min-width: 0; }
.activities-item > img { display: block; margin-bottom: 10px; width: 100%; height: 200px; object-fit: cover; border-radius: 8px; }
.activities-item p { font-size: 0.88em; color: #666; margin: 0; font-weight: bold; line-height: 1.3; }
@media (max-width: 768px) { .activities-item { flex: 0 0 100%; } }

/* ---- carousel ---- */
.slide-view { position: relative; width: 100%; overflow: hidden; border-radius: 8px; margin-bottom: 10px; height: 200px; background: #f3f3f3; }
.slide-track { display: flex; height: 100%; will-change: transform; }
.slide-track img { height: 100%; object-fit: cover; display: block; min-width: 0; }
/* 2 images: pure-CSS back-and-forth */
.slide-view[data-count="2"] .slide-track { width: 200%; animation: slide2 6s ease-in-out infinite; }
@keyframes slide2 { 0%,42% {transform:translateX(0);} 50%,92% {transform:translateX(-50%);} 100% {transform:translateX(0);} }
/* 3+ images: JS-driven loop */
.slide-view[data-count]:not([data-count="2"]) .slide-track { width: calc(var(--n,3) * 100%); transition: transform .55s ease-in-out; }
.slide-view[data-count]:not([data-count="2"]) .slide-track img { flex: 0 0 calc(100% / var(--n,3)); }
@media (prefers-reduced-motion: reduce) {
  .slide-view[data-count="2"] .slide-track { animation: none !important; transform: none !important; }
  .slide-view[data-count]:not([data-count="2"]) .slide-track { transition: none !important; }
}
</style>

<div class="activities-scroll">
  <div class="activities-container">
     <!-- ③ 轮播卡片：3 张图（JS 顺序循环，记得 data-count 和 --n 都要等于张数） -->
    <div class="activities-item">
      <div class="slide-view" data-count="3" data-interval="4000" style="--n:3;">
        <div class="slide-track">
          <img src="../images/activities/valse1.jpg" alt="">
          <img src="../images/activities/valse2.jpg" alt="">
          <img src="../images/activities/valse3.jpg" alt="">
        </div>
      </div>
      <p>VALSE2026(Wuhan·2026.05)</p>
    </div>
    <!-- ① 单张图卡片 -->
    <div class="activities-item">
      <img src="../images/activities/qingyun.jpg" alt="VALSE 2026">
      <p>Tencent QingYun Program(Beijing·2026.03)</p>
    </div>
    <div class="activities-item">
      <img src="../images/activities/Outstanding Student Model.jpg" alt="VALSE 2026">
      <p>Outstanding Student Model(Chengdu·2024.12)</p>
    </div>
    
    <!-- ② 轮播卡片：2 张图（纯 CSS 来回切） -->
    <div class="activities-item">
      <div class="slide-view" data-count="2">
        <div class="slide-track">
          <img src="../images/activities/qingyun1.jpg" alt="">
          <img src="../images/activities/qingyun2.jpg" alt="">
        </div>
      </div>
      <p>Tencent QingYun Program, Beijing · 2026.03</p>
    </div>
    
    <!-- ③ 轮播卡片：3 张图（JS 顺序循环，记得 data-count 和 --n 都要等于张数） -->
    <div class="activities-item">
      <div class="slide-view" data-count="3" data-interval="4000" style="--n:3;">
        <div class="slide-track">
          <img src="../images/activities/wave1.jpg" alt="">
          <img src="../images/activities/wave2.jpg" alt="">
          <img src="../images/activities/wave3.jpg" alt="">
        </div>
      </div>
      <p>WAVE Summit 2025, Beijing</p>
    </div>

  </div>
</div>
<div style="margin-top: 5px; font-size: small; color:#888;">⬆ Scrollable</div>

<script>
(function () {
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  document.querySelectorAll(".slide-view[data-count]").forEach(function (view) {
    var n = parseInt(view.getAttribute("data-count"), 10);
    if (!n || n <= 2) return;            // 2 张由 CSS 动画处理
    var track = view.querySelector(".slide-track");
    if (!track) return;
    var ms = parseInt(view.getAttribute("data-interval") || "4000", 10);
    var i = 0;
    setInterval(function () {
      i = (i + 1) % n;
      track.style.transform = "translateX(calc(-100% * " + i + " / " + n + "))";
    }, ms);
  });
})();
</script>
