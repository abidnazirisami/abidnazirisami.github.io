---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---

<section class="masthead" aria-label="Profile">
  <img class="masthead__photo" src="{{ '/assets/Edited_Formal.png' | relative_url }}"
       alt="M M Abid Naziri" width="512" height="512">
  <div class="masthead__body">
    <p class="masthead__where">
      Room 3228, Koch Hall (EB2) <br/>
      <img class="inline-logo" src="{{ '/favicon.ico' | relative_url }}" alt="" aria-hidden="true"> NC State University<br/>
      Raleigh, USA
    </p>
    <ul class="contact-links">
      <li><i class="fas fa-graduation-cap" aria-hidden="true"></i><a href="https://scholar.google.com/citations?hl=en&user=oJJIZNcAAAAJ" target="_blank" rel="noopener">Google Scholar</a></li>
      <li><i class="fas fa-envelope" aria-hidden="true"></i><a href="mailto:abidnazirisami@gmail.com">abidnazirisami@gmail.com</a></li>
      <li><i class="fas fa-university" aria-hidden="true"></i><a href="mailto:mnaziri@ncsu.edu">mnaziri@ncsu.edu</a></li>
      <li><i class="fab fa-github" aria-hidden="true"></i><a href="https://github.com/abidnazirisami" target="_blank" rel="noopener">github.com/abidnazirisami</a></li>
      <li><i class="fab fa-linkedin" aria-hidden="true"></i><a href="https://www.linkedin.com/in/abidnazirisami" target="_blank" rel="noopener">linkedin.com/in/abidnazirisami</a></li>
    </ul>
  </div>
</section>

<section class="news-card" aria-labelledby="news-heading">
  <div class="news-card__head">
    <h2 class="news-card__title" id="news-heading">Latest highlights</h2>
    <span class="news-card__meta">Last updated: November 13, 2026</span>
  </div>
  {% capture news_md %}{% include news.md %}{% endcapture %}
  <div class="news-card__scroll scroll-panel" tabindex="0" role="region" aria-labelledby="news-heading">
    {{ news_md | markdownify }}
  </div>
</section>

<h2 id="about">Who am I?</h2>

I am a fifth-year PhD candidate at [NC State](https://www.ncsu.edu/), where I work with [Dr. Marcelo d'Amorim](https://damorim.github.io/) in the [Software Engineering Group](https://ncsu.software/). My area of research is software testing. My dissertation focuses on finding bugs in deep learning libraries such as PyTorch, TensorFlow, and JAX. Before the PhD, I worked for more than three years as a Senior Software Engineer at [Enosis Solutions](https://www.enosisbd.com/). I expect to graduate in May 2027.

<h2 id="research">Research Interests</h2>

<p class="lede">I love finding bugs in complex software.</p>

My passion is developing testing techniques that reveal these bugs. Complex software is hard to test: its inputs must satisfy many constraints, and there is often no simple way to tell whether an output is correct. Deep learning libraries, compilers, databases, and LLM serving engines are examples of complex software where I have found bugs using the techniques I developed and studied. I report each bug to the developers so that it gets fixed, and this is how I help build more robust software.

<h2 id="trophy-case">🏆 Trophy Case</h2>

These are the bugs I have reported to the developers of open-source software, as of {{ site.data.bug_stats.generated | date: "%B %Y" }} ([full list](/bugs/)).

{% include trophy_case.html %}

<h2 id="publications">Publications</h2>

<div class="pub-list" markdown="1">
{% include publications_list.md %}
</div>

<!-- <h1>Education and Experience</h1>

 I completed my undergraduate degree in [Computer Science and Engineering](https://du.ac.bd/body/CSE) from [University of Dhaka](https://du.ac.bd) in 2018. After graduating, I worked as a Senior Software Engineer at [Enosis Solutions](https://www.enosisbd.com/). I used to work with several desktop applications written primarily in `Delphi`, with other desktop applications and web apps involving technologies like `ASP.NET Core`, `React JS` etc. -->
