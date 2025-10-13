- BugsInDLLs : A Database of Reproducible Bugs in Deep Learning Libraries to Enable Systematic Evaluation of Testing Techniques\
[M M Abid Naziri](/), Aman Kumar Singh, [Feiran Qin](https://nsdi.dev/), Benjamin Wu, [Saikat Dutta](https://www.cs.cornell.edu/~saikatd/), [Marcelo d'Amorim](https://damorim.github.io/)\
We introduce BugsInDLLs, a curated database of **112** reproducible bugs from popular deep learning libraries like TensorFlow and PyTorch. This benchmark provides the research community with a standard resource to systematically evaluate and improve bug-finding techniques.\
**Published** in [ISSTA 2025, Tool Demonstration](https://conf.researchr.org/details/issta-2025/issta-2025-tool-demonstrations/7/BugsInDLLs-A-Database-of-Reproducible-Bugs-in-Deep-Learning-Libraries-to-Enable-Sys)\
<a class="btn" href="{{ '/papers/bugsindlls.pdf' | relative_url }}" target="_blank" rel="noopener">[PDF]</a> [[Tool]](https://github.com/ncsu-swat/bugsindlls)
- Evaluating the Effectiveness of Neurosymbolic Constraint Learning for Testing Deep Learning Library APIs\
[M M Abid Naziri](/), [Shinhae Kim](https://shinhae-kim.github.io/), [Feiran Qin](https://nsdi.dev/), [Saikat Dutta](https://www.cs.cornell.edu/~saikatd/), [Marcelo d'Amorim](https://damorim.github.io/)\
This paper introduces a novel neurosymbolic technique to test Deep Learning library APIs by dynamically learning their input constraints. By uniquely combining a grammar-guided Large Language Model with an SMT solver, the technique generates more valid and diverse test inputs than prior approaches. Our method significantly improves API and code coverage and has already found **23** new bugs in PyTorch and TensorFlow, **11** of which have been confirmed.\
_Submitted_
- Testing Autonomous Driving Systems with Focused Misbehavior Forecasting\
[M M Abid Naziri](/), [Stefano Carlo Lambertenghi](https://www.fortiss.org/en/results/scientific-publications/author/stefano-carlo-lambertenghi), [Andrea Stocco](https://tsigalko18.github.io/), [Marcelo d'Amorim](https://damorim.github.io/)\
This paper introduces a testing technique for autonomous driving systems that identifies potential failures by forecasting and fuzzing "near-miss" events in simulation. By using a misbehavior forecaster to target high-risk scenarios, our approach makes testing more efficient and effective. In our evaluation using the CARLA simulator, Foresee finds up to **128%** more failures than baselines while being up to **2.49x** faster, and improves the bug-finding capability of state-of-the-art fuzzers by over **93%**.\
_Submitted_
- Evaluating the Effectiveness of Coverage-Guided Fuzzing for Testing Deep Learning Library APIs\
[Feiran Qin](https://nsdi.dev/), [M M Abid Naziri](/), [Saikat Dutta](https://www.cs.cornell.edu/~saikatd/), [Marcelo d'Amorim](https://damorim.github.io/)\
This work presents the first in-depth study confirming the effectiveness of Coverage-Guided Fuzzing (CGF) for testing Deep Learning library APIs. We introduce FlashFuzz, a novel tool that makes this possible by using Large Language Models (LLMs) to automatically synthesize and repair the required test harnesses. Our approach vastly outperforms state-of-the-art fuzzers in code coverage (up to **+212%**) and speed (up to **1182x**), leading to the discovery of **42** new bugs in PyTorch and TensorFlow.\
_Submitted_ \
[[Preprint]](https://arxiv.org/abs/2509.14626) [[PDF]](https://arxiv.org/pdf/2509.14626)
