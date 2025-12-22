def condition(context):
  return True

def run(context):
  if 'actions' in context and len(context['actions']) > 0:
    for action in context['actions']:
      action(context)
  else:
    print('no actions yet')

def _while(condition, run):
  context = {}
  while condition(context):
    run(context)

_while(
  condition,
  run
)
