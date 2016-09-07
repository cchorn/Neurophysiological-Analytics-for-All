FROM andrewosh/binder-base

USER root

# Add dependencies
RUN apt-get update
RUN conda install -c http://conda.anaconda.org/r r-essentials
RUN conda install xlwt pytables cython scikit-learn
RUN pip install neo quantities sqlalchemy-migrate pywavelets
RUN pip install OpenElectrophy # this breaks if quantities is not installed first
RUN conda install -c https://conda.anaconda.org/r rpy2
RUN wget https://cran.r-project.org/src/contrib/ez_4.3.tar.gz
RUN R CMD INSTALL ez_4.3.tar.gz
RUN wget https://cran.r-project.org/src/contrib/R2HTML_2.3.2.tar.gz
RUN R CMD INSTALL R2HTML_2.3.2.tar.gz
RUN wget https://cran.r-project.org/src/contrib/gss_2.1-5.tar.gz
RUN R CMD INSTALL gss_2.1-5.tar.gz
RUN wget https://cran.r-project.org/src/contrib/STAR_0.3-7.tar.gz
RUN R CMD INSTALL STAR_0.3-7.tar.gz
RUN conda install -c https://conda.anaconda.org/r r-survival # conda seems to work best
