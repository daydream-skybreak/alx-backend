import { createQueue } from 'kue'
export default function createPushNotificationJobs(jobs, queue){
    if (! Array.isArray(jobs)) throw new Error("Jobs is not an array")
    jobs.forEach(item => {
        let job = queue.create('push_notification_code_3', item)
        job
            .on('enqueue', () => {
                console.log('Notification job created:', job.id)
            })
            .on('complete', () => {
                console.log(`Notification job ${job.id} complete`)
            })
            .on('failed attempt', (err) => {
                console.log(`Notification job ${job.id} failed:`,
                    err.message || err.toString())
            })
            .on('progress', (prog, data) => {
                console.log(`Notification job ${job.id} ${prog}% complete`)
            });
        job.save();
        }
    )
}

