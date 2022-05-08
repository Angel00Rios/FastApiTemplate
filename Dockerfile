FROM registry.cirrus.ibm.com/ubi8/python-38

# Change to root for the following tasks.
USER root

# Containers get UTC as default, so set it to the usual timezone.
ENV TZ=America/Mexico_City
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# -- [Required]
ENV APP=/app
COPY . $APP

RUN mkdir -p $APP/data $APP/ssh

# Speed up download and instalation of dependencies, if possible.
COPY ./requirements.txt $APP/
RUN pip install --upgrade pip && \
    pip install -r $APP/requirements.txt --no-cache-dir

# The runtime user ID is random with an assigned user group of 0.
RUN chgrp -R 0 $APP && chmod -R g=u $APP

ENV PYTHONPATH=$APP/app

CMD sh $APP/api.sh