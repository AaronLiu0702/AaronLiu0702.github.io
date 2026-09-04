<style>
  .paper-topics {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-top: 8px;
    margin-bottom: 4px;
  }

  .paper-topic {
    display: inline-flex;
    align-items: center;
    padding: 3px 10px;
    border: 1px solid #3182ce;
    border-radius: 7px;
    background-color: #ebf8ff;
    color: #2b6cb0;
    font-size: 13px;
    font-weight: 600;
    line-height: 1.4;
    white-space: nowrap;
  }

  
  .paper-badge {
    display: inline-block;
    padding: 4px 10px;
    color: #8a6200;
    background-color: #fff4c2;
    border: 1px solid #f1d675;
    border-radius: 8px;
    font-size: 13px;
    font-weight: 600;
    line-height: 1.4;
    text-decoration: none !important;
    transition: all 0.2s ease;
  }

  .paper-badge:hover {
    color: #704f00;
    background-color: #ffe99a;
    border-color: #e5c34f;
    text-decoration: none !important;
    transform: translateY(-1px);
  }

 /* ===== 链接按钮基础样式 ===== */
  .btn-link {
      display: inline-block;
      padding: 2px 9px;
      margin-right: 2px;
      font-size: 0.85em;
      font-weight: 600;
      letter-spacing: 0.02em;
      line-height: 1.55;
      border-radius: 4px;
      border-bottom: 0 !important;
      text-decoration: none !important;
      transition: filter 0.15s ease;
  }

  .btn-link:hover,
  .btn-link:focus {
      border-bottom: 0 !important;
      text-decoration: none !important;
      filter: brightness(0.94);        /* hover 时轻微变暗 */
  }

  /* 关键：抵消 minimal-mistakes 主题给正文链接加的下划线/阴影 */
  .page__content .btn-link,
  .page__content .btn-link:hover,
  .page__content .btn-link:focus,
  .paper-box .btn-link,
  .paper-box .btn-link:hover,
  .paper-box .btn-link:focus {
      border-bottom: 0 !important;
      box-shadow: none !important;
      text-decoration: none !important;
  }

  /* ===== 各类型按钮配色（底色 + 文字色）===== */
  .btn-paper, .btn-paper:hover { background: #E8F0FE; color: #1A73E8; }
  .btn-code,  .btn-code:hover  { background: #E8EAED; color: #3C4043; }
  .btn-home,  .btn-home:hover  { background: #EDE7F6; color: #7B61C9; }
  .btn-hf,    .btn-hf:hover    { background: #FEEFE3; color: #B06000; }
  .btn-bib,   .btn-bib:hover   { background: #E8EAF6; color: #3F51B5; cursor: pointer; }

  /* ===== 按钮内嵌图标（HF logo）===== */
  .btn-link img {
      height: 1.05em;
      width: auto;
      vertical-align: -0.15em;
      margin-right: 4px;
      box-shadow: none;
  }

  .btn-link img:only-child {
      margin-right: 0;                 /* 图标后没文字时不留空隙 */
  }

  /* BIB 悬停弹窗 */
  .bib-tooltip {
      position: absolute;
      z-index: 1000;
      display: none;
      max-width: 520px;
      padding: 10px 14px;
      background: #fff;
      border: 1px solid #e0e0e0;
      border-radius: 6px;
      box-shadow: 0 6px 18px rgba(0, 0, 0, 0.12);
      font-family: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
      font-size: 0.78em;
      line-height: 1.5;
      color: #333;
      white-space: pre-wrap;
      pointer-events: none;
  }
  </style>

# 🔥 News

- **2026.08:**  🎉🎉  One paper has been accepted by **<span style="color:red">ICONIP 2026</span>**!
- **2026.07:**  ✈️✈️  I was honored to be invited to participate in the **<span style="color:red">Qingyun|UBIQuent|Apex Intelligence Talent Dinner</span>** at ICML 2026!
- **2026.05:**  ✈️✈️  I was honored to be invited to participate in the "AI Talent Corner" at VALSE 2026!
- **2026.04:**  🧩🧩  We released [**General365**](https://general365.github.io/), advancing LLM reasoning beyond domain-specific tasks toward general real-world scenarios.
- **2026.04:**  🎉🎉  One paper has been accepted by **<span style="color:red">ACL 2026</span>**! [**AMO-Bench**](https://amo-bench.github.io/)！
- **2026.03:**  🎉🎉  One paper has been accepted by **<span style="color:red">IJCNN 2026</span>**! [**ACE-MAPPO**](https://arxiv.org/abs/2605.25091v1)！
- **2026.03:**  ✈️✈️  I was honored to be invited to participate in the **<span style="color:red">Tencent QingYun Talent Program</span>**! “Stars of the Future”
- **2025.06:**  🎉🎉  I received my B.E. degree from Sichuan Agricultural University (SICAU), awarded the Outstanding Graduate and Outstanding Thesis Award, ranking <strong style="color: red;">1<sup>st</sup>/198</strong> in overall GPA for three years (2022-2025) !  🌟🌟[**Student Spotlight**](https://mp.weixin.qq.com/s/M3Csv3M7xnbveIlspLem6w)🌟🌟



# 📝 Publications 

<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge" style="background-color: rgb(231, 77, 60); color: white; font-weight: bold;">
        ACL 2026 (CCF-A)
      </div>
      <a href="https://amo-bench.github.io/"><img src='images/AMO-Bench.png' alt="sym" width="100%"></a>
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
  
  **<img src="../images/longcat.svg" alt="icon" style="height:25px; vertical-align:middle;"> AMO-Bench: Large Language Models Still Struggle in High School Math Competitions.**  
  
  🧑‍💻 <ins>**Junlin Liu**</ins>, Shengnan An, Shuang Zhou, Dan Ma, Yehao Lin, Xinxuan Lv, Xuanlin Wang, Xiaoyu Li, Ziwen Wang, Xuezhi Cao, Xunliang Cai.
  <br>
  🏛️ **<span style="color: rgb(165, 28, 48);">The 64th Annual Meeting of the Association for Computational Linguistics, 2026.</span>**
  <div class="paper-topics">
    <span class="paper-topic"><b>CCF-A</b></span>
    <span class="paper-topic">Mathematical Reasoning</span>
    <span class="paper-topic">LLM Evaluation</span>
  </div>

  [Paper](https://aclanthology.org/2026.findings-acl.101/){:.btn-link .btn-paper}
  [Code](https://github.com/meituan-longcat/AMO-Bench){:.btn-link .btn-code}
  [ProjectPage](https://amo-bench.github.io/){:.btn-link .btn-home}
  [<img src='images/icon/huggingface.svg' alt="">HF](https://huggingface.co/datasets/meituan-longcat/AMO-Bench){:.btn-link .btn-hf}
  <a href="#" class="btn-link btn-bib" data-bib-key="liu2026amo">BIB</a>
[![Stars](https://img.shields.io/github/stars/meituan-longcat/AMO-Bench?style=flat&label=Stars)](https://github.com/meituan-longcat/AMO-Bench)
[![Citations](https://img.shields.io/badge/Citations-40-EBB215)](https://arxiv.org/abs/2510.26768)
  </div>
</div>



<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge" style="background-color: rgb(231, 77, 60); color: white; font-weight: bold;">
        EMNLP 2026 (Under Review)
      </div>
      <a href="https://general365.github.io/"><img src='images/General365.png' alt="sym" width="100%"></a>
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
  
  **<img src="../images/longcat.svg" alt="icon" style="height:25px; vertical-align:middle;"> General365: Benchmarking General Reasoning in LLMs Across Diverse and Challenging Tasks.**  
  
  🧑‍💻 <ins>**Junlin Liu**</ins>, Shengnan An, Shuang Zhou, Dan Ma, Shixiong Luo, Ying Xie, Yuan Zhang, Wenling Yuan, Yifan Zhou, Xiaoyu Li, Ziwen Wang, Xuezhi Cao, Xunliang Cai.
  <br>
  <div class="paper-topics">
    <span class="paper-topic">General Reasoning</span>
    <span class="paper-topic">LLM Evaluation</span>
  </div>
  
[Paper](https://arxiv.org/abs/2604.11778){:.btn-link .btn-paper}
[Code](https://github.com/meituan-longcat/General365){:.btn-link .btn-code}
[ProjectPage](https://general365.github.io/){:.btn-link .btn-home}
[<img src='images/icon/huggingface.svg' alt="">HF](https://huggingface.co/datasets/meituan-longcat/General365_Public){:.btn-link .btn-hf}
<a href="#" class="btn-link btn-bib" data-bib-key="liu2026general365">BIB</a>
[![Stars](https://img.shields.io/github/stars/meituan-longcat/General365?style=flat&label=Stars)](https://github.com/meituan-longcat/General365)
[![Citations](https://img.shields.io/badge/Citations-6-EBB215)](https://arxiv.org/abs/2604.11778)
  </div>
</div>



<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge" style="background-color: rgb(231, 77, 60); color: white; font-weight: bold;">
        AAAI 2027 (Under Review)
      </div>
      <a href="https://arxiv.org/abs/2607.28026"><img src='images/CRPO.png' alt="sym" width="100%"></a>
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
  
  **<img src="../images/longcat.svg" alt="icon" style="height:25px; vertical-align:middle;"> Contrastive Reinforced Policy Optimization via Privileged Self-Distillation.**  
  
  🧑‍💻 Xingjian Wu*, <ins>**Junlin Liu***</ins>, Xingchen Liu, Xuhang Zhu, Jianing Wang, Linsen Guo, Xiaoyu Li, <br>Xuezhi Cao, Xunliang Cai.
  <br>
  <div class="paper-topics">
    <span class="paper-topic">Agentic RL</span>
    <span class="paper-topic">On-Policy Self-Distillation</span>
    <span class="paper-topic">Contrastive Policy Optimization</span>
  </div>
[Paper](https://arxiv.org/abs/2607.28026){:.btn-link .btn-paper}
<a href="#" class="btn-link btn-bib" data-bib-key="wu2026contrastive">BIB</a>
  </div>
</div>



<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge" style="background-color: rgb(231, 77, 60); color: white; font-weight: bold;">
        AAAI 2027 (Under Review)
      </div>
      <a href="https://arxiv.org/abs/2607.24280"><img src='images/MAPD.png' alt="sym" width="100%"></a>
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
  
  **<img src="../images/qwen.svg" alt="icon" style="height:22px; vertical-align:middle;"> From Proprietary to Open-Source: Bridging the Distribution Gap via Multi-Agent Protocol Distillation in Agentic Search.**  
  
  🧑‍💻 <ins>**Junlin Liu**</ins>, Chunji Lv, Jiangwang Chen, Zixin Song, Shuaiyu Zhou, Xingjian Wu, Kailin Jiang, <br>Jinyang Wu, Bohan yu, Chenxi Zhou, Xiao Yang, Da Zhu, Guanjun Jiang.
  <br>
   <div class="paper-topics">
    <span class="paper-topic">Agentic Search</span>
    <span class="paper-topic">On-Policy Self-Distillation</span>
    <span class="paper-topic">Multi-Agent Systems</span>
     <a class="paper-badge"
       href="https://huggingface.co/papers/2607.24280"
       target="_blank"
       rel="noopener noreferrer">
      🤗 #3 Paper of the Day
    </a>
  </div>
  
[Paper](https://arxiv.org/abs/2607.24280){:.btn-link .btn-paper}
[Code](https://github.com/AaronLiu0702/MAPD){:.btn-link .btn-code}
[<img src='images/icon/huggingface.svg' alt="">HF](https://huggingface.co/papers/2607.24280){:.btn-link .btn-hf}
<a href="#" class="btn-link btn-bib" data-bib-key="liu2026proprietary">BIB</a>
[![Stars](https://img.shields.io/github/stars/AaronLiu0702/MAPD?style=flat&label=Stars)](https://github.com/AaronLiu0702/MAPD)
[![Citations](https://img.shields.io/badge/Citations-4-EBB215)](https://arxiv.org/abs/2607.24280)
  </div>
</div>



<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge" style="background-color: rgb(231, 77, 60); color: white; font-weight: bold;">
        AAAI 2027 (Under Review)
      </div>
      <a href="https://arxiv.org/abs/2607.25675"><img src='images/paper_overview/Decoevo.png' alt="sym" width="100%"></a>
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
  
  **<img src="../images/qwen.svg" alt="icon" style="height:22px; vertical-align:middle;"> DecoEvo: Score-Decoupled Co-Evolution of Solver and Rubric-Generator Skills in Text Space.**  
  
  🧑‍💻 Jiangwang Chen\*, Zixin Song\*, <ins>**Junlin Liu**\*</ins>, Shuaiyu Zhou, Haiyan Wu, Haihan Shi, Chenxi Zhou, Hanqing Li, Xiao Yang, Da Zhu, Guanjun Jiang.
  <br>
  <div class="paper-topics">
    <span class="paper-topic">LLM Agents</span>
    <span class="paper-topic">Self-Evolving Agent</span>
    <span class="paper-topic">Skill and Rubric Learning</span>
  </div>

[Paper](https://arxiv.org/abs/2607.25675){:.btn-link .btn-paper}
[<img src='images/icon/huggingface.svg' alt="">HF](https://huggingface.co/papers/2607.25675){:.btn-link .btn-hf}
<a href="#" class="btn-link btn-bib" data-bib-key="chen2026decoevo">BIB</a>
[![Citations](https://img.shields.io/badge/Citations-2-EBB215)](https://arxiv.org/abs/2607.25675)
  </div>
</div>



<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge" style="background-color: rgb(231, 77, 60); color: white; font-weight: bold;">
        AAAI 2027 (Under Review)
      </div>
      <img src='images/paper_overview/HarnessOpt.png' alt="sym" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
  
  **<img src="../images/qwen.svg" alt="icon" style="height:25px; vertical-align:middle;"> HarnessOpt: Long-Horizon Harness Self-Improvement via Accumulated Optimizer State.**  
  
  🧑‍💻 Shuaiyu Zhou\*, Jiaying Zhang\*, <ins>**Junlin Liu**\*</ins>, Jiangwang Chen, Zixin Song, Haiyan Wu, Hanqing Li, Jinzhou Song, Xiao Yang, Da Zhu, Guanjun Jiang.
  <br>
  <div class="paper-topics">
    <span class="paper-topic">LLM Agents</span>
    <span class="paper-topic">Self-Evolving Agent</span>
    <span class="paper-topic">Harness Engineering</span>
  </div>
  </div>
</div>




<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge" style="background-color: rgb(231, 77, 60); color: white; font-weight: bold;">
        AAAI 2027 (Under Review)
      </div>
      <a href="https://arxiv.org/abs/2608.01837"><img src='images/paper_overview/PCSD.png' alt="sym" width="100%"></a>
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
  
  **<img src="../images/longcat.svg" alt="icon" style="height:25px; vertical-align:middle;"> PCSD: Persistent Consistency for Self-Distillation in Agentic Reinforcement Learning.**  
  
  🧑‍💻 Chunji Lv\*, Yangguang Wei\*, <ins>**Junlin Liu**\*</ins>, Yang Gao, Ming Liu, Xinming Wang, Jinyang Wu, <br>Guoren Wang, Changsheng Li.
  <br>
  <div class="paper-topics">
    <span class="paper-topic">Agentic RL</span>
    <span class="paper-topic">On-Policy Self-Distillation</span>
    <span class="paper-topic">Adaptive Weighting</span>
  </div>
[Paper](https://arxiv.org/abs/2608.01837){:.btn-link .btn-paper}
[<img src='images/icon/huggingface.svg' alt="">HF](https://huggingface.co/papers/2608.01837){:.btn-link .btn-hf}
<a href="#" class="btn-link btn-bib" data-bib-key="lv2026pcsd">BIB</a>
  </div>
</div>



<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge" style="background-color: rgb(231, 77, 60); color: white; font-weight: bold;">
        KDD 2027 (Under Review)
      </div>
      <a href="https://arxiv.org/abs/2607.28037"><img src='images/paper_overview/ClawTrack.png' alt="sym" width="100%"></a>
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
  
  **<img src="../images/longcat.svg" alt="icon" style="height:25px; vertical-align:middle;"> ClawTrack: Towards Trace-Level Evaluation and Improvement of Real-World Autonomous Agents.**  
  
  🧑‍💻 Xingjian Wu, Xuhang Zhu, Xingchen Liu, <ins>**Junlin Liu**</ins>, Jianing Wang, Linsen Guo, Xiaoyu Li, <br>Xuezhi Cao, Xunliang Cai.
  <br>
  <div class="paper-topics">
    <span class="paper-topic">Agent Evaluation</span>
    <span class="paper-topic">Long-Horizon Agent</span>
    <span class="paper-topic">Real-World interaction</span>
  </div>
[Paper](https://arxiv.org/abs/2607.28037){:.btn-link .btn-paper}
[ProjectPage](https://1997-hank-wu.github.io/ClawTrack-Leaderboard/){:.btn-link .btn-home}
<a href="#" class="btn-link btn-bib" data-bib-key="wu2026clawtrack">BIB</a>
  </div>
</div>



<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge" style="background-color: rgb(231, 77, 60); color: white; font-weight: bold;">
        AAAI 2027 (Under Review)
      </div>
      <a href="https://arxiv.org/pdf/2607.19747"><img src='images/paper_overview/Rubric_set.png' alt="sym" width="100%"></a>
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
  
  **<img src="../images/icon/tencent.svg" alt="icon" style="height:25px; vertical-align:middle;"> Beyond Relevance-Centric Retrieval: Rubric-Oriented Document Set Selection and Ranking.**  
  
  🧑‍💻 Kailin Jiang, Lei Liu, Jian Xi, Hui Xu, <ins>**Junlin Liu**</ins>, Baochen Fu, Shaoqing Ren, Bin Li, Vichwang, <br>Yu Lu, Haibo Shi.
  <br>
  <div class="paper-topics">
    <span class="paper-topic">Retrieval-Augmented Generation</span>
    <span class="paper-topic">Retrieval Evaluation</span>
    <span class="paper-topic">Rubric-Guided</span>
  </div>
[Paper](https://arxiv.org/pdf/2607.19747){:.btn-link .btn-paper}
[Code](https://github.com/Rubric4Setwise/Rubric4Setwise){:.btn-link .btn-code}
[ProjectPage](https://rubric4setwise.github.io/){:.btn-link .btn-home}
[<img src='images/icon/huggingface.svg' alt="">HF](https://huggingface.co/collections/placeholder){:.btn-link .btn-hf}
<a href="#" class="btn-link btn-bib" data-bib-key="jiang2026beyond">BIB</a>
[![Stars](https://img.shields.io/github/stars/Rubric4Setwise/Rubric4Setwise?style=flat&label=Stars)](https://github.com/Rubric4Setwise/Rubric4Setwise)
[![Citations](https://img.shields.io/badge/Citations-1-EBB215)](https://arxiv.org/abs/2607.19747)
  </div>
</div>


<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge" style="background-color: rgb(231, 77, 60); color: white; font-weight: bold;">
        AAAI 2027 (Under Review)
      </div>
      <a href="https://arxiv.org/abs/2608.12996"><img src='images/paper_overview/ATOBench.png' alt="sym" width="100%"></a>
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
  
  **<img src="../images/alibaba.svg" alt="icon" style="height:30px; vertical-align:middle;"> ATOBench: Tracing How Autonomous Penetration-Testing Agents Verify Vulnerabilities When Target Evidence Lies.**  
  
  🧑‍💻 Qiyang Chen, Yixi Li, Fengwei Zhang, <ins>**Junlin Liu**</ins>.
  <br>
  <div class="paper-topics">
    <span class="paper-topic">Agent Evaluation</span>
    <span class="paper-topic">Penetration Testing</span>
    <span class="paper-topic">Agent Security</span>
  </div>
[Paper](https://arxiv.org/abs/2608.12996){:.btn-link .btn-paper}
[Code](https://github.com/daxtar2/ATOBench){:.btn-link .btn-code}
<a href="#" class="btn-link btn-bib" data-bib-key="chen2026atobench">BIB</a>
  </div>
</div>


<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge" style="background-color: rgb(231, 77, 60); color: white; font-weight: bold;">
        AAAI 2027 (Under Review)
      </div>
      <img src='images/paper_overview/HalluAgent.png' alt="sym" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
  
  **<img src="../images/alibaba.svg" alt="icon" style="height:30px; vertical-align:middle;"> HalluAgent: Type-Conditioned Visual Evidence for Hallucination Mitigation in Large Vision-Language Models.**  
  
  🧑‍💻 Ruipeng Zhang, Zhangtianyi Chen, Zixuan Huang, Tong Ji, <ins>**Junlin Liu**</ins>, Yuhao Shen, YiQiLiao, <br>Bailin Liang, Ruibo Duan.
  <br>
  <div class="paper-topics">
    <span class="paper-topic">Multi-modal Agents</span>
    <span class="paper-topic">Agent Hallucination</span>
    <span class="paper-topic">Tool-Use</span>
  </div>
  </div>
</div>


<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge" style="background-color: rgb(231, 77, 60); color: white; font-weight: bold;">
        AAAI 2027 (Under Review)
      </div>
      <a href="https://arxiv.org/abs/2607.14327"><img src='images/PReM.png' alt="sym" width="100%"></a>
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
  
  **<img src="../images/alibaba.svg" alt="icon" style="height:30px; vertical-align:middle;"> PReM: Learning What to Preserve and When to Refresh for Context Compression.**  
  
  🧑‍💻 Bohan Yu*, Lei Shen*, Chenxi Zhou, Chen Han, <ins>**Junlin Liu**</ins>, Wenbo Su, Yu Cheng, Bo Zheng.
  <br>
  <div class="paper-topics">
    <span class="paper-topic">Long-Context LLM</span>
    <span class="paper-topic">Context Compression</span>
    <span class="paper-topic">LLM Memory</span>
  </div>
[Paper](https://arxiv.org/abs/2607.14327){:.btn-link .btn-paper}
[Code](){:.btn-link .btn-code}
<a href="#" class="btn-link btn-bib" data-bib-key="yu2026prem">BIB</a>
  </div>
</div>




<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge" style="background-color: rgb(231, 77, 60); color: white; font-weight: bold;">
        ICONIP 2026 (CCF-C)
      </div>
      <a href=""><img src='images/DRG-MAPPO.png' alt="sym" width="100%"></a>
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
  
  **<img src="../images/ucas.svg" alt="icon" style="height:25px; vertical-align:middle;"> DRG-MAPPO: Hierarchical Dynamic Role-Graph Multi-Agent Reinforcement Learning for Cooperative Air Combat.**  
  
  🧑‍💻 <ins>**Junlin Liu**</ins>, Yang Gao, Chengwei Li, Hui Chang, Xinchen Zhang, Zhijun Zhao, Hao Zhao.
  <br>
  🏛️ **<span style="color: rgb(165, 28, 48);">International Conference on Neural Information Processing, 2026.</span>**
  <div class="paper-topics">
    <span class="paper-topic">CCF-C</span>
    <span class="paper-topic">Reinforce Learning</span>
    <span class="paper-topic">Multi-Agent System</span>
    <span class="paper-topic">Agent Collaboration and Game</span>
  </div>
  </div>
</div>



<div class='paper-box'>
  <div class='paper-box-image'>
    <div>
      <div class="badge" style="background-color: rgb(231, 77, 60); color: white; font-weight: bold;">
        IJCNN 2026 (CCF-C)
      </div>
      <a href="https://arxiv.org/abs/2605.25091"><img src='images/ACE-MAPPO.png' alt="sym" width="100%"></a>
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
  
  **<img src="../images/ucas.svg" alt="icon" style="height:25px; vertical-align:middle;"> Evolutionary Enhanced Multi-Agent Reinforcement Learning for Cooperative Air Combat.**  
  🧑‍💻 Chengwei Li*, <ins>**Junlin Liu***</ins>, Yang Gao, Hui Chang, Xinchen Zhang, Hao Zhao.
  <br>
  🏛️ **<span style="color: rgb(165, 28, 48);">International Joint Conference on Neural Networks, 2026.</span>**
  <div class="paper-topics">
    <span class="paper-topic">CCF-C</span>
    <span class="paper-topic">Reinforce Learning</span>
    <span class="paper-topic">Multi-Agent System</span>
    <span class="paper-topic">Agent Collaboration and Game</span>
  </div>
  [Paper](https://arxiv.org/abs/2605.25091){:.btn-link .btn-paper}
  <a href="#" class="btn-link btn-bib" data-bib-key="li2026evolutionary">BIB</a>
  </div>
</div>


