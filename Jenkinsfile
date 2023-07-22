pipeline {
  agent any
  stages {
    stage ('Docker Login') {
      steps {
        withDockerRegistry([credentialsId: 'dockerIDCred', url: ""]){
        }
      }
    }
   
    stage ('Build Image') {
      steps {
        sh 'docker build -t dnerorepo/python-apps .'
      }
    }

    stage ('Pubilsh Image') {
      steps {
        sh 'docker push dnerorepo/python-apps'
      }
    }

    stage ('Remove Unwanted Images') {
      steps {
        sh 'docker rmi -f $(docker images -q)'
      }
    }
  }
}




       //      stage ('Build and Push Image') {
       //      steps {
       //           withDockerRegistry([credentialsId: 'DOCKERHUB_USERNAME', url: ""]) {
       //             sh 'docker build -t ${REPOSITORY_TAG} .'
       //             sh 'docker push ${REPOSITORY_TAG}'          
       //      }
       //    }
       // }
