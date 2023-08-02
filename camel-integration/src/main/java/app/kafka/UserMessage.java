package app.kafka;

import java.time.Instant;

public class UserMessage {
   private String action;
   private String entity;
   private UserData data;

   public String getAction() {
      return action;
   }

   public void setAction(String action) {
      this.action = action;
   }

   public String getEntity() {
      return entity;
   }

   public void setEntity(String entity) {
      this.entity = entity;
   }

   public UserData getData() {
      return data;
   }

   public void setData(UserData data) {
      this.data = data;
   }

   public static class UserData {
      private String user_id;
      private String username;
      private String email;
      private Instant created_at;
      private Instant updated_at;
      private Instant deleted_at;

      public String getUser_id() {
         return user_id;
      }

      public void setUser_id(String user_id) {
         this.user_id = user_id;
      }

      public String getUsername() {
         return username;
      }

      public void setUsername(String username) {
         this.username = username;
      }

      public String getEmail() {
         return email;
      }

      public void setEmail(String email) {
         this.email = email;
      }

      public Instant getCreated_at() {
         return created_at;
      }

      public void setCreated_at(Instant created_at) {
         this.created_at = created_at;
      }

      public Instant getUpdated_at() {
         return updated_at;
      }

      public void setUpdated_at(Instant updated_at) {
         this.updated_at = updated_at;
      }

      public Instant getDeleted_at() {
         return deleted_at;
      }

      public void setDeleted_at(Instant deleted_at) {
         this.deleted_at = deleted_at;
      }
   }
}
