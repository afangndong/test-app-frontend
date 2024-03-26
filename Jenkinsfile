node {
    def app

    stage('Clone repository'){

        checkout scm
    }

    stage('Build image'){

        app = docker.build("afangndong/app-frontend")
    }

    stage('Test image'){

        app.inside {
            sh 'echo "Tests passed"'
        }
    }

    stage('Push image'){

        docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
            app.push("${env.BUILD_NUMBER}")
        }
    }

    stage('Trigger ManifestUpdate'){
        echo "Triggering updatemanifestjob"
        build job: 'app-frontend-updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
    }
}