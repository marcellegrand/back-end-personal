const app = require('./app');
require('./lib/mongooselib');

async function main() {
    let port = app.get('port');
    await app.listen(port);
    console.log(`Server running on http://localhost:${port}`);
}

main();