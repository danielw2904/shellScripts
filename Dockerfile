FROM rocker/shiny:latest
  
RUN R -e "install.packages(c('xtable', 'ggplot2'), repos = 'https://cran.rstudio.com/')"
