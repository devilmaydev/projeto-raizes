## Checkpoints — save no slot «checkpoint»; game over (Sim) carrega esse save.
##
## Nos marcos seguros:
##     $ jussara_checkpoint()
##     $ jussara_checkpoint("abordagem_jussara")

define JUSSARA_CHECKPOINT_SLOT = "checkpoint"

init python:
    def jussara_checkpoint(nome=None):
        """Grava checkpoint no slot fixo (e tenta autosave como cópia de segurança)."""
        if getattr(renpy.store, "_in_replay", False):
            return
        if nome is not None:
            store.last_checkpoint_name = nome
        extra = nome if nome else "Checkpoint"
        renpy.save(JUSSARA_CHECKPOINT_SLOT, extra)
        try:
            renpy.force_autosave(take_screenshot=True)
        except Exception:
            pass

    def jussara_checkpoint_slot_to_load():
        """Slot a carregar no game over: checkpoint dedicado, senão último auto-*."""
        if renpy.can_load(JUSSARA_CHECKPOINT_SLOT):
            return JUSSARA_CHECKPOINT_SLOT
        return renpy.newest_slot(regexp=r"^auto")

    def jussara_game_over_continue():
        slot = jussara_checkpoint_slot_to_load()
        if slot is None or not renpy.can_load(slot):
            return False
        renpy.load(slot)
        return True


default last_checkpoint_name = None
