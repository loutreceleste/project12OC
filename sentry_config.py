import sentry_sdk


def initialize_sentry():
    sentry_sdk.init(
        dsn="https://a49ffe0270f6d84209c9d810d6b0c407@o4506913525727232.ingest.us.sentry.io/4506914023014400",
        traces_sample_rate=1.0,
        profiles_sample_rate=1.0,
    )
