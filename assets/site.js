(() => {
 const c=window.HEALTH360_CONFIG||{};
 const d=document.getElementById("health360-dashboard-viz"), s=document.getElementById("health360-story-viz");
 const dl=document.getElementById("dashboard-direct"), sl=document.getElementById("story-direct"), rl=document.getElementById("repo-link");
 if(c.dashboardUrl){d?.setAttribute("src",c.dashboardUrl);dl?.setAttribute("href",c.dashboardUrl);}
 if(c.storyUrl){s?.setAttribute("src",c.storyUrl);sl?.setAttribute("href",c.storyUrl);}
 if(c.repositoryUrl)rl?.setAttribute("href",c.repositoryUrl);
})();