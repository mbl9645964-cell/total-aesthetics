/* Total Aesthetics — Cosmetic & Dental Clinic — site interactions */
(function(){
  "use strict";

  document.addEventListener("DOMContentLoaded", function(){

    /* Sticky header shadow */
    var header = document.querySelector(".site-header");
    if(header){
      var onScroll = function(){ header.classList.toggle("scrolled", window.scrollY > 8); };
      onScroll();
      window.addEventListener("scroll", onScroll, { passive:true });
    }

    /* Mobile nav drawer */
    var toggle = document.querySelector("[data-nav-toggle]");
    var drawer = document.querySelector("[data-mobile-nav]");
    var scrim = document.querySelector("[data-nav-scrim]");
    var closeBtn = document.querySelector("[data-nav-close]");
    function setNav(open){
      if(drawer) drawer.classList.toggle("open", open);
      if(scrim) scrim.classList.toggle("show", open);
      if(toggle) toggle.setAttribute("aria-expanded", open ? "true" : "false");
      document.body.style.overflow = open ? "hidden" : "";
    }
    if(toggle) toggle.addEventListener("click", function(){ setNav(!drawer.classList.contains("open")); });
    if(closeBtn) closeBtn.addEventListener("click", function(){ setNav(false); });
    if(scrim) scrim.addEventListener("click", function(){ setNav(false); });
    document.querySelectorAll(".mobile-nav a").forEach(function(a){ a.addEventListener("click", function(){ setNav(false); }); });

    /* Reveal on scroll, with stagger index for grid children */
    document.querySelectorAll(".stagger").forEach(function(g){
      Array.prototype.forEach.call(g.children, function(c,i){ c.style.setProperty("--i", i); });
    });
    var reveals = document.querySelectorAll("[data-reveal]");
    if("IntersectionObserver" in window && reveals.length){
      var io = new IntersectionObserver(function(entries){
        entries.forEach(function(e){
          if(e.isIntersecting){ e.target.classList.add("in"); io.unobserve(e.target); }
        });
      }, { threshold:.1, rootMargin:"0px 0px -6% 0px" });
      reveals.forEach(function(el){ io.observe(el); });
    } else {
      reveals.forEach(function(el){ el.classList.add("in"); });
    }

    /* Hero slideshow */
    var slideshow = document.querySelector("[data-hero-slideshow]");
    if(slideshow){
      var slides = slideshow.querySelectorAll(".hero__slide");
      var dotsWrap = document.querySelector("[data-hero-dots]");
      var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      if(slides.length > 1){
        var i = 0, timer = null, DELAY = 4800;
        var dots = [];
        if(dotsWrap){
          slides.forEach(function(_, idx){
            var b = document.createElement("button");
            b.type = "button";
            b.setAttribute("aria-label", "Slide " + (idx+1));
            if(idx === 0) b.classList.add("is-active");
            b.addEventListener("click", function(){ go(idx); reset(); });
            dotsWrap.appendChild(b);
            dots.push(b);
          });
        }
        var go = function(n){
          slides[i].classList.remove("is-active");
          if(dots[i]) dots[i].classList.remove("is-active");
          i = (n + slides.length) % slides.length;
          slides[i].classList.add("is-active");
          if(dots[i]) dots[i].classList.add("is-active");
        };
        var next = function(){ go(i+1); };
        var start = function(){ if(!reduce){ timer = setInterval(next, DELAY); } };
        var reset = function(){ clearInterval(timer); start(); };
        start();
        document.addEventListener("visibilitychange", function(){
          if(document.hidden){ clearInterval(timer); } else { start(); }
        });
      }
    }

    /* Animated counters (facts, steps) */
    var counters = document.querySelectorAll("[data-count]");
    if("IntersectionObserver" in window && counters.length){
      var co = new IntersectionObserver(function(entries){
        entries.forEach(function(e){
          if(!e.isIntersecting) return;
          co.unobserve(e.target);
          var el = e.target;
          var target = parseFloat(el.getAttribute("data-count"));
          var suffix = el.getAttribute("data-suffix") || "";
          var dur = 1200, t0 = null;
          function step(ts){
            if(!t0) t0 = ts;
            var p = Math.min((ts - t0) / dur, 1);
            var eased = 1 - Math.pow(1 - p, 3);
            el.textContent = Math.round(target * eased) + suffix;
            if(p < 1) requestAnimationFrame(step);
            else el.textContent = target + suffix;
          }
          requestAnimationFrame(step);
        });
      }, { threshold:.6 });
      counters.forEach(function(el){ co.observe(el); });
    }

    /* WhatsApp enquiry form -> opens WhatsApp with the message */
    document.querySelectorAll("form[data-wa-form]").forEach(function(f){
      f.addEventListener("submit", function(e){
        e.preventDefault();
        var name = (f.querySelector('[name="name"]') || {}).value || "";
        var msg = (f.querySelector('[name="message"]') || {}).value || "";
        var text = "Hello Total Aesthetics, my name is " + name + ". " + msg;
        var url = "https://wa.me/919999999999?text=" + encodeURIComponent(text.trim());
        window.open(url, "_blank", "noopener");
        var note = f.querySelector(".form__msg");
        if(note){ note.classList.add("ok"); note.textContent = "Opening WhatsApp so you can send this straight to our team."; }
      });
    });

  });
})();
