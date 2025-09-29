---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---

<!-- styles moved to assets/css/custom.css and loaded via assets/main.scss -->

<div class="hero">
    <img class="hero-photo" src="/assets/Edited_Formal.png" alt="M M Abid Naziri">
    <aside class="hero-contacts" aria-label="Contacts">
        <div class="hero-location" aria-label="Office Location">
            <p>
                Room 3228, Engineering Bldg II<br/>
                NC State University<br/>
                Raleigh, USA
            </p>
        </div>
        <ul class="contact-links">
            <li><i class="fas fa-graduation-cap"></i><a href="https://scholar.google.com/citations?hl=en&user=oJJIZNcAAAAJ" target="_blank" rel="noopener">Google Scholar</a></li>
            <li><i class="fas fa-envelope"></i><a href="mailto:abidnazirisami@gmail.com">abidnazirisami@gmail.com</a></li>
            <li><i class="fas fa-university"></i><a href="mailto:mnaziri@ncsu.edu">mnaziri@ncsu.edu</a></li>
            <li><i class="fab fa-github"></i><a href="https://github.com/abidnazirisami" target="_blank" rel="noopener">github.com/abidnazirisami</a></li>
            <li><i class="fab fa-linkedin"></i><a href="https://www.linkedin.com/in/abidnazirisami" target="_blank" rel="noopener">linkedin.com/in/abidnazirisami</a></li>
        </ul>
    </aside>
    <aside class="hero-news" aria-label="News">
        <div class="hero-news-list">
            <h3>News</h3>
            {% capture news_md %}{% include news.md %}{% endcapture %}
            {{ news_md | markdownify }}
            <div class="meta">Latest highlights</div>
        </div>
    </aside>
</div>
<h1>Who am I?</h1>
 I am a fourth year PhD Student at [NC State](https://www.ncsu.edu/). I am working with [Dr. Marcelo D'Amorim](https://damorim.github.io/) as a member of the [Software Engineering Group](https://ncsu.software/). My area of research is Software Testing.

<h1>Research Interests</h1>

 My overall research interest lies in testing learning enabled system. I am working on various testing techniques to find bugs in Deep Learning Libraries such as PyTorch, Tensorflow, Jax etc. To date, I have reported 48 bugs in PyTorch and Tensorflow ([full list of reported bugs](https://docs.google.com/spreadsheets/d/1r03ajIybbPeLBqHdxbD54Qghwoy8NjL2weeh89vX7wM/edit?usp=sharing)). I am also working in generating complex test cases for Autonomous Driving Systems (ADS).

<h1>Publications</h1>

{% include publications_list.md %}


<h1>Education and Experience</h1>

 I completed my undergraduate degree in Computer Science and Engineering from University of Dhaka in 2018. After graduating, I worked as a Senior Software Engineer at [Enosis Solutions](https://www.enosisbd.com/). I used to work with several desktop applications written primarily in `Delphi`, with other desktop applications and web apps involving technologies like `ASP.NET Core`, `React JS` etc.