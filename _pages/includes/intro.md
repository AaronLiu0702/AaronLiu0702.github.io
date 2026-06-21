
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

/* ---- carousel (unified: 2 张和 3+ 张都由 JS 驱动) ---- */
.slide-view { position: relative; width: 100%; overflow: hidden; border-radius: 8px; margin-bottom: 10px; height: 200px; background: #f3f3f3; }
.slide-track {
  display: flex; height: 100%; will-change: transform;
  width: calc(var(--n,2) * 100%);
  transition: transform .55s ease-in-out;
}
.slide-track img { height: 100%; object-fit: cover; display: block; flex: 0 0 calc(100% / var(--n,2)); min-width: 0; }
@media (prefers-reduced-motion: reduce) { .slide-track { transition: none !important; } }
</style>

<div class="activities-scroll">
  <div class="activities-container">
    <!-- ② 轮播卡片：2 张图 -->
    <div class="activities-item">
      <div class="slide-view" data-count="2" style="--n:2;">
        <div class="slide-track">
          <img src="../images/activities/UCAS2026.jpg" alt="">
          <img src="../images/activities/UCAS202602.jpg" alt="">
        </div>
      </div>
      <p>
        中国科学院大学 人工智能学院 (北京·2026.06)
      </p>
    </div>
    <!-- ② 轮播卡片：2 张图 -->
    <div class="activities-item">
      <div class="slide-view" data-count="2" style="--n:2;">
        <div class="slide-track">
          <img src="../images/activities/alistar2026.jpg" alt="">
          <img src="../images/activities/alistar20262.jpg" alt="">
        </div>
      </div>
      <p>
        <a href="https://mp.weixin.qq.com/s/_YP_MzFDGz5jZImE7hYadg" target="_blank">阿里星热爱之旅</a>
        (北京·2026.05)
      </p>
    </div>
     <!-- ③ 轮播卡片：3 张图 -->
    <div class="activities-item">
      <div class="slide-view" data-count="3" style="--n:3;">
        <div class="slide-track">
          <img src="../images/activities/valse1.jpg" alt="">
          <img src="../images/activities/valse2.jpg" alt="">
          <img src="../images/activities/valse3.jpg" alt="">
        </div>
      </div>
      <p>
        <a href="https://www.xiaohongshu.com/explore/6a117406000000003600109f?note_flow_source=wechat&xsec_token=CBc7sUmRT9tKrESqVvdRL30GH7cm5gZuAz_YVgmLQttqw=" target="_blank">VALSE2026</a>
        (武汉·2026.05)
      </p>
    </div>
    <!-- ④ 单张图卡片 -->
    <div class="activities-item">
      <img src="../images/activities/qingyun.jpg" alt="腾讯青云计划">
      <p>腾讯青云计划 (北京·2026.03)</p>
    </div>
    <!-- ⑤ 单张图卡片 -->
    <div class="activities-item">
      <img src="../images/activities/Outstanding Student Model.jpg" alt="Outstanding Student Model">
      <p>
        <a href="https://mp.weixin.qq.com/s/M3Csv3M7xnbveIlspLem6w" target="_blank">优秀学生标兵</a>
        (成都·2024.12)
      </p>
    </div>
  </div>
</div>

<script>
(function () {
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  var INTERVAL = 4000;   // ★ 统一的切换间隔（毫秒）。想全局调速只改这一个数字
  document.querySelectorAll(".slide-view[data-count]").forEach(function (view) {
    var n = parseInt(view.getAttribute("data-count"), 10);
    if (!n || n < 2) return;
    var track = view.querySelector(".slide-track");
    if (!track) return;
    var ms = parseInt(view.getAttribute("data-interval") || INTERVAL, 10);
    var i = 0;
    setInterval(function () {
      i = (i + 1) % n;
      track.style.transform = "translateX(calc(-100% * " + i + " / " + n + "))";
    }, ms);
  });
})();
</script>
