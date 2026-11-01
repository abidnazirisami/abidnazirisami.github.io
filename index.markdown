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
      Room 3228, Engineering Bldg II<br/>
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
    <span class="news-card__meta">Last updated: April 25, 2026</span>
  </div>
  {% capture news_md %}{% include news.md %}{% endcapture %}
  <div class="news-card__scroll scroll-panel" tabindex="0" role="region" aria-labelledby="news-heading">
    {{ news_md | markdownify }}
  </div>
</section>

<h2>Who am I?</h2>
 I am a fifth year PhD Student at [NC State](https://www.ncsu.edu/). I am working with [Dr. Marcelo D'Amorim](https://damorim.github.io/) as a member of the [Software Engineering Group](https://ncsu.software/). My area of research is Software Testing.

<h2>Research Interests</h2>

 My overall research interest lies in testing learning enabled system. I am working on various testing techniques to find bugs in Deep Learning Libraries such as PyTorch, Tensorflow, Jax etc.
 I have also worked on testing applications in domains like databases, compilers, toolchains etc. using Property-Based Testing. In addition,
 I have worked on generating complex test cases for Autonomous Driving Systems (ADS). To date, I have reported 323 bugs across 11 systems including deep learning frameworks, databases, compilers, and toolchains, with 214 confirmed or fixed upstream ([list of bug-reports](/bugs/)).

<h2>Publications</h2>

<div class="pub-list" markdown="1">
{% include publications_list.md %}
</div>

<!-- <h1>Education and Experience</h1>

 I completed my undergraduate degree in [Computer Science and Engineering](https://du.ac.bd/body/CSE) from [University of Dhaka](https://du.ac.bd) in 2018. After graduating, I worked as a Senior Software Engineer at [Enosis Solutions](https://www.enosisbd.com/). I used to work with several desktop applications written primarily in `Delphi`, with other desktop applications and web apps involving technologies like `ASP.NET Core`, `React JS` etc. -->
