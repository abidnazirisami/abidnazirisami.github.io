- Testing Deep Learning Libraries via Neurosymbolic Constraint Learning\
    [M M Abid Naziri](/)<sup>\*</sup>, [Shinhae Kim](https://shinhae-kim.github.io/)<sup>\*</sup>, [Feiran Qin](https://nsdi.dev/), [Saikat Dutta](https://www.cs.cornell.edu/~saikatd/), [Marcelo d'Amorim](https://damorim.github.io/)\
    *IEEE/ACM International Conference on Software Engineering (accpt. 21.8% [321/1469])*\
    ([ICSE 2026](https://conf.researchr.org/details/icse-2026/icse-2026-research-track/272/Testing-Deep-Learning-Libraries-via-Neurosymbolic-Constraint-Learning)), Rio de Janeiro, Brazil, April 2026.\
    [[Preprint]](https://arxiv.org/abs/2601.15493) [[PDF]](https://arxiv.org/pdf/2601.15493)\
    <details>
    <summary>Summary</summary>
        This paper introduces <b>Centaur</b>, a novel neurosymbolic technique to test Deep Learning library APIs by dynamically learning their input constraints. By uniquely combining a grammar-guided Large Language Model with an SMT solver, Centaur generates more valid and diverse test inputs than prior approaches. Our method significantly improves API and code coverage and has already found <b>26</b> new bugs in PyTorch and TensorFlow, <b>18</b> of which have been confirmed.
    </details>
- Misbehavior Forecasting for Focused Autonomous Driving Systems Testing\
    [M M Abid Naziri](/), [Stefano Carlo Lambertenghi](https://www.fortiss.org/en/results/scientific-publications/author/stefano-carlo-lambertenghi), [Andrea Stocco](https://tsigalko18.github.io/), [Marcelo d'Amorim](https://damorim.github.io/)\
    *IEEE/ACM International Conference on Software Engineering (accpt. 21.8% [321/1469])*\
    ([ICSE 2026](https://conf.researchr.org/details/icse-2026/icse-2026-research-track/301/Misbehavior-Forecasting-for-Focused-Autonomous-Driving-Systems-Testing)), Rio de Janeiro, Brazil, April 2026.\
    [[Preprint]](https://arxiv.org/abs/2512.18823) [[PDF]](https://arxiv.org/pdf/2512.18823)\
    <details>
    <summary>Summary</summary>
        This paper introduces <b>Foresee</b>, a testing technique for autonomous driving systems that identifies potential failures by forecasting and fuzzing "near-miss" events in simulation. By using a misbehavior forecaster to target high-risk scenarios, our approach makes testing more efficient and effective. In our evaluation using the CARLA simulator, Foresee finds up to <b>128%</b> more failures than baselines while being up to <b>2.49x</b> faster, and improves the bug-finding capability of state-of-the-art fuzzers by over <b>93%</b>.
    </details>
- BugsInDLLs : A Database of Reproducible Bugs in Deep Learning Libraries to Enable Systematic Evaluation of Testing Techniques\
    [M M Abid Naziri](/), Aman Kumar Singh, [Feiran Qin](https://nsdi.dev/), Benjamin Wu, [Saikat Dutta](https://www.cs.cornell.edu/~saikatd/), [Marcelo d'Amorim](https://damorim.github.io/)\
    *International Symposium on Software Testing and Analysis (Tool Demos)*\
    ([ISSTA 2025, Tool Demonstration](https://conf.researchr.org/details/issta-2025/issta-2025-tool-demonstrations/7/BugsInDLLs-A-Database-of-Reproducible-Bugs-in-Deep-Learning-Libraries-to-Enable-Sys)), Trondheim, Norway, June 2025.\
    <a class="btn" href="{{ '/papers/bugsindlls.pdf' | relative_url }}" target="_blank" rel="noopener">[PDF]</a> [[Tool]](https://github.com/ncsu-swat/bugsindlls)
    <details>
    <summary>Summary</summary>
        We introduce <b>BugsInDLLs</b>, a curated database of <b>112</b> reproducible bugs from popular deep learning libraries like TensorFlow and PyTorch. This benchmark provides the research community with a standard resource to systematically evaluate and improve bug-finding techniques.
    </details>
- Improving Deep Learning Library Testing with Machine Learning\
    [Facundo Molina](https://facumolina.github.io/), [M M Abid Naziri](/), [Feiran Qin](https://nsdi.dev/), [Alessandra Gorla](https://software.imdea.org/~alessandra.gorla/), [Marcelo d'Amorim](https://damorim.github.io/)\
    *ACM/IEEE International Conference on Automation of Software Test (accpt. 40% [18/45])*\
    ([AST 2026](https://conf.researchr.org/home/ast-2026)), Rio de Janeiro, Brazil, April 2026.\
    <a class="btn" href="{{ '/papers/specs4freeDLL.pdf' | relative_url }}" target="_blank" rel="noopener">[PDF]</a>
    <details>
    <summary>Summary</summary>
        This paper demonstrates the effectiveness of ML classifiers as an efficient validity checker for DL Library inputs. Once trained with enough data, different out-of-the-box classifiers can achieve high accuracy in predicting whether an input will be valid or not without executing the input on an API. We demonstrate that the classifiers can predict the validity of an input with an accuracy of <b>91%</b>. We also improve <a href="https://github.com/shijy16/ACETest">ACETest</a>, a prominent DL Library API fuzzing tool, by complementing the technique with ML classifiers. The validity ratio of the tool increases from <b>29%</b> to <b>61%</b> after the integration, demonstrating the effectiveness of ML classifiers as a filter for the DL Library API inputs.
    </details>
- Evaluating the Effectiveness of Coverage-Guided Fuzzing for Testing Deep Learning Library APIs\
[Feiran Qin](https://nsdi.dev/), [M M Abid Naziri](/), [Saikat Dutta](https://www.cs.cornell.edu/~saikatd/), [Marcelo d'Amorim](https://damorim.github.io/)\
    _Submitted_ \
    [[Preprint]](https://arxiv.org/abs/2509.14626) [[PDF]](https://arxiv.org/pdf/2509.14626)\
    <details>
    <summary>Summary</summary>
        This work presents the first in-depth study confirming the effectiveness of Coverage-Guided Fuzzing (CGF) for testing Deep Learning library APIs. We introduce FlashFuzz, a novel tool that makes this possible by using Large Language Models (LLMs) to automatically synthesize and repair the required test harnesses. Our approach vastly outperforms state-of-the-art fuzzers in code coverage (up to <b>+212%</b>) and speed (up to <b>1182x</b>), leading to the discovery of <b>42</b> new bugs in PyTorch and TensorFlow.
    </details>

<font size="1.5"><sup>*</sup>Equal contribution</font>