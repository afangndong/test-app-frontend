node{
    def app

    stage('Clone Repository'){

        checkout scm
    }

    stage('Update GIT'){
        script {
            catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                withCredentials([usernamePassword(credentialsId: 'github', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
                    //def encodePAssword = URL.encode("$GIT_PASSWORD", 'UTF-8')
                    sh "git config user.email clemsbrass@yahoo.fr"
                    sh "git config user.name 'Clement Afang Ndong'"

                    //git switch to master
                    sh "cat deployment.yaml"
                    sh "sed -i 's+afangndong/app-frontend.*+afangndong/app-frontend:${DOCKERTAG}+g' deployment.yaml"
                    sh "cat deployment.yaml"
                    sh "git add ."
                    sh "git commit -m 'Done by Jenkins Job changemanifest: ${env.BUILD_NUMBER}'"
                    sh "git push https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/${GIT_USERNAME}/Manifest/app-frontend-updatemanifest.git HEAD:main"
                }
            }
        }
    }
}