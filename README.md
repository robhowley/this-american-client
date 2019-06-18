# this american client
the [this american life](https://www.thisamericanlife.org/) client library

## Install

```bash
pip install this-american-life
```

## Using the client

### Get the transcript of an episode
```python
from thisamericanlife import ThisAmericanLife

tal = ThisAmericanLife()
ep_one_transcript = tal.transcripts.get(episode_number=1)

print(ep_one_transcript.transcript)
```
