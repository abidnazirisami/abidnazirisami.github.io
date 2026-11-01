1. <span class="pub-title">A Multi-Domain Study on the Effectiveness of LLMs at Writing Property-Based Tests</span> <span class="pub-links"><a href="https://arxiv.org/pdf/2610.34487"><i class="fa fa-file-pdf" aria-hidden="true"></i> pdf</a> <a href="https://anonymous.4open.science/r/pbt-study-artifact-6A0B"><i class="fa fa-tools" aria-hidden="true"></i> tool</a></span>
    <span class="pub-authors">[M M Abid Naziri](/), [Feiran Qin](https://nsdi.dev/), Khush Patel, [Marcelo d'Amorim](https://damorim.github.io/)</span>
    <span class="pub-venue">*Submitted for review*</span>

    <details class="disclosure">
    <summary>Summary</summary>
    <div class="disclosure__body" markdown="0">
        This paper presents a multi-domain study of how well LLMs generalize as Property-Based Test (PBT) writers. We use <a href="https://arxiv.org/pdf/2307.04346">Proptest-AI</a> and <a href="https://arxiv.org/pdf/2510.09907?">Agentic-PBT</a>, two LLM-based methods for writing PBTs, as instruments to test <b>10</b> applications from <b>5</b> domains: deep learning libraries, databases, system software, compilers, and LLM serving engines. We filed <b>180</b> bug reports, <b>44</b> of which duplicate reports others filed after the models' knowledge cutoffs; maintainers have confirmed <b>65</b> of the remaining reports, spanning all <b>5</b> domains, and fixed <b>23</b>. Comparing against domain-specific fuzzers, we find that the fuzzers cover more of the compilers and of PostgreSQL but less of PyTorch than Agentic-PBT, and that low observability is the main obstacle for LLM-based PBT writers.
    </div>
    </details>
2. <span class="pub-title">A Comprehensive Study of Bugs from Deep Learning Library Fuzzers</span>
    <span class="pub-authors">[M M Abid Naziri](/), Manideepika Reddy Myaka, [Lingjun Liu](https://lingjunliu.github.io/), [Saikat Dutta](https://www.cs.cornell.edu/~saikatd/), [Marcelo d'Amorim](https://damorim.github.io/)</span>
    <span class="pub-venue">*Submitted for review*</span>

    <details class="disclosure">
    <summary>Summary</summary>
    <div class="disclosure__body" markdown="0">
        We present a large-scale empirical study of <b>220</b> bugs reported by five state-of-the-art Deep Learning library testing techniques, reproducing each bug and analyzing its triggering input and root cause. We find that <b>70%</b> of the bugs are validation bugs triggered by simple invalid-input patterns rather than deep logic errors, and identify <b>94</b> distinct input patterns capable of triggering them. Exploiting these patterns, we build a mutational fuzzing tool that uncovers <b>46</b> new bugs in Deep Learning libraries, <b>30</b> of which have been confirmed.
    </div>
    </details>
3. <span class="pub-title">How Effective Is Coverage-Guided Fuzzing to Test Deep Learning Library APIs?</span> <span class="pub-links"><a href="{{ '/papers/flashfuzz-icst2026.pdf' | relative_url }}" target="_blank" rel="noopener"><i class="fa fa-file-pdf" aria-hidden="true"></i> pdf</a> <a href="https://github.com/ncsu-swat/flashfuzz"><i class="fa fa-tools" aria-hidden="true"></i> tool</a></span>
    <span class="pub-authors">[Feiran Qin](https://nsdi.dev/), [M M Abid Naziri](/), [Saikat Dutta](https://www.cs.cornell.edu/~saikatd/), [Marcelo d'Amorim](https://damorim.github.io/)</span>
    <span class="pub-award">🏆 IEEE Computer Society TCSE Best Student Paper Award</span>
    <span class="pub-venue">*IEEE International Conference on Software Testing, Verification and Validation (accpt. 26.9% [44/163])*</span>
    <span class="pub-where">[ICST 2026](https://conf.researchr.org/home/icst-2026), Daejeon, Republic of Korea, May 2026.</span>

    <details class="disclosure">
    <summary>Summary</summary>
    <div class="disclosure__body" markdown="0">
        This work presents the first in-depth study confirming the effectiveness of Coverage-Guided Fuzzing (CGF) for testing Deep Learning library APIs. We introduce FlashFuzz, a novel tool that makes this possible by using Large Language Models (LLMs) to automatically synthesize and repair the required test harnesses. Our approach vastly outperforms state-of-the-art fuzzers in code coverage (up to <b>+212%</b>) and speed (up to <b>1182x</b>), leading to the discovery of <b>42</b> new bugs in PyTorch and TensorFlow.
    </div>
    </details>
4. <span class="pub-title">Testing Deep Learning Libraries via Neurosymbolic Constraint Learning</span> <span class="pub-links"><a href="https://arxiv.org/pdf/2601.15493"><i class="fa fa-file-pdf" aria-hidden="true"></i> pdf</a> <a href="https://github.com/ncsu-swat/centaur"><i class="fa fa-tools" aria-hidden="true"></i> tool</a></span>
    <span class="pub-authors">[M M Abid Naziri](/)<sup>\*</sup>, [Shinhae Kim](https://shinhae-kim.github.io/)<sup>\*</sup>, [Feiran Qin](https://nsdi.dev/), [Saikat Dutta](https://www.cs.cornell.edu/~saikatd/), [Marcelo d'Amorim](https://damorim.github.io/)</span>
    <span class="pub-venue">*IEEE/ACM International Conference on Software Engineering (accpt. 21.8% [321/1469])*</span>
    <span class="pub-where">[ICSE 2026](https://conf.researchr.org/details/icse-2026/icse-2026-research-track/272/Testing-Deep-Learning-Libraries-via-Neurosymbolic-Constraint-Learning), Rio de Janeiro, Brazil, April 2026.</span>

    <details class="disclosure">
    <summary>Summary</summary>
    <div class="disclosure__body" markdown="0">
        This paper introduces <b>Centaur</b>, a novel neurosymbolic technique to test Deep Learning library APIs by dynamically learning their input constraints. By uniquely combining a grammar-guided Large Language Model with an SMT solver, Centaur generates more valid and diverse test inputs than prior approaches. Our method significantly improves API and code coverage and has already found <b>26</b> new bugs in PyTorch and TensorFlow, <b>18</b> of which have been confirmed.
    </div>
    </details>
5. <span class="pub-title">Misbehavior Forecasting for Focused Autonomous Driving Systems Testing</span> <span class="pub-links"><a href="https://arxiv.org/pdf/2512.18823"><i class="fa fa-file-pdf" aria-hidden="true"></i> pdf</a> <a href="https://github.com/ncsu-swat/foresee"><i class="fa fa-tools" aria-hidden="true"></i> tool</a></span>
    <span class="pub-authors">[M M Abid Naziri](/), [Stefano Carlo Lambertenghi](https://www.fortiss.org/en/results/scientific-publications/author/stefano-carlo-lambertenghi), [Andrea Stocco](https://tsigalko18.github.io/), [Marcelo d'Amorim](https://damorim.github.io/)</span>
    <span class="pub-venue">*IEEE/ACM International Conference on Software Engineering (accpt. 21.8% [321/1469])*</span>
    <span class="pub-where">[ICSE 2026](https://conf.researchr.org/details/icse-2026/icse-2026-research-track/301/Misbehavior-Forecasting-for-Focused-Autonomous-Driving-Systems-Testing), Rio de Janeiro, Brazil, April 2026.</span>

    <details class="disclosure">
    <summary>Summary</summary>
    <div class="disclosure__body" markdown="0">
        This paper introduces <b>Foresee</b>, a testing technique for autonomous driving systems that identifies potential failures by forecasting and fuzzing "near-miss" events in simulation. By using a misbehavior forecaster to target high-risk scenarios, our approach makes testing more efficient and effective. In our evaluation using the CARLA simulator, Foresee finds up to <b>128%</b> more failures than baselines while being up to <b>2.49x</b> faster, and improves the bug-finding capability of state-of-the-art fuzzers by over <b>93%</b>.
    </div>
    </details>
6. <span class="pub-title">Improving Deep Learning Library Testing with Machine Learning</span> <span class="pub-links"><a href="https://arxiv.org/pdf/2602.03755"><i class="fa fa-file-pdf" aria-hidden="true"></i> pdf</a> <a href="https://sites.google.com/view/ml4dllconstraints"><i class="fa fa-tools" aria-hidden="true"></i> tool</a></span>
    <span class="pub-authors">[Facundo Molina](https://facumolina.github.io/), [M M Abid Naziri](/), [Feiran Qin](https://nsdi.dev/), [Alessandra Gorla](https://software.imdea.org/~alessandra.gorla/), [Marcelo d'Amorim](https://damorim.github.io/)</span>
    <span class="pub-venue">*ACM/IEEE International Conference on Automation of Software Test (accpt. 40% [18/45])*</span>
    <span class="pub-where">[AST 2026](https://conf.researchr.org/details/ast-2026/ast-2026-papers/4/Improving-Deep-Learning-Library-Testing-with-Machine-Learning), Rio de Janeiro, Brazil, April 2026.</span>

    <details class="disclosure">
    <summary>Summary</summary>
    <div class="disclosure__body" markdown="0">
        This paper demonstrates the effectiveness of ML classifiers as an efficient validity checker for DL Library inputs. Once trained with enough data, different out-of-the-box classifiers can achieve high accuracy in predicting whether an input will be valid or not without executing the input on an API. We demonstrate that the classifiers can predict the validity of an input with an accuracy of <b>91%</b>. We also improve <a href="https://github.com/shijy16/ACETest">ACETest</a>, a prominent DL Library API fuzzing tool, by complementing the technique with ML classifiers. The validity ratio of the tool increases from <b>29%</b> to <b>61%</b> after the integration, demonstrating the effectiveness of ML classifiers as a filter for the DL Library API inputs.
    </div>
    </details>
7. <span class="pub-title">BugsInDLLs : A Database of Reproducible Bugs in Deep Learning Libraries to Enable Systematic Evaluation of Testing Techniques</span> <span class="pub-links"><a href="{{ '/papers/bugsindlls.pdf' | relative_url }}" target="_blank" rel="noopener"><i class="fa fa-file-pdf" aria-hidden="true"></i> pdf</a> <a href="https://github.com/ncsu-swat/bugsindlls"><i class="fa fa-tools" aria-hidden="true"></i> tool</a></span>
    <span class="pub-authors">[M M Abid Naziri](/), Aman Kumar Singh, [Feiran Qin](https://nsdi.dev/), Benjamin Wu, [Saikat Dutta](https://www.cs.cornell.edu/~saikatd/), [Marcelo d'Amorim](https://damorim.github.io/)</span>
    <span class="pub-venue">*International Symposium on Software Testing and Analysis (Tool Demos)*</span>
    <span class="pub-where">[ISSTA 2025, Tool Demonstration](https://conf.researchr.org/details/issta-2025/issta-2025-tool-demonstrations/7/BugsInDLLs-A-Database-of-Reproducible-Bugs-in-Deep-Learning-Libraries-to-Enable-Sys), Trondheim, Norway, June 2025.</span>

    <details class="disclosure">
    <summary>Summary</summary>
    <div class="disclosure__body" markdown="0">
        We introduce <b>BugsInDLLs</b>, a curated database of <b>112</b> reproducible bugs from popular deep learning libraries like TensorFlow and PyTorch. This benchmark provides the research community with a standard resource to systematically evaluate and improve bug-finding techniques.
    </div>
    </details>

<p class="pub-footnote"><sup>*</sup>Equal contribution</p>
